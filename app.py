import streamlit as st
import time
from datetime import datetime

# ✅ 무조건 첫 Streamlit 명령어
st.set_page_config(
    page_title="PwC 뉴스 분석기",
    page_icon="📊",
    layout="wide",
)


# 프롬프트 템플릿 정의
CUSTOM_PROMPT_TEMPLATE = '''당신은 회계법인의 전문 애널리스트입니다. 아래 뉴스 목록을 분석하여 회계법인 관점에서 가장 중요한 뉴스를 선별하세요. 

[선택 기준]
{selection_criteria}

[제외 대상]
{exclusion_criteria}

[응답 요구사항]
1. 선택 기준에 부합하는 뉴스가 많다면 최대 3개까지 선택 가능합니다.
2. 선택 기준에 부합하는 뉴스가 없다면, 그 이유를 명확히 설명해주세요.

[응답 형식]
다음과 같은 JSON 형식으로 응답해주세요:

{{
    "selected_news": [
        {{
            "index": 1,
            "title": "뉴스 제목",
            "press": "언론사명",
            "date": "발행일자",
            "reason": "선정 사유",
            "keywords": ["키워드1", "키워드2"]
        }},
        ...
    ],
    "excluded_news": [
        {{
            "index": 2,
            "title": "뉴스 제목",
            "reason": "제외 사유"
        }},
        ...
    ]
}}

[유효 언론사]
{valid_press}

[중복 처리 기준]
{duplicate_handling}'''

from news_ai import (
    collect_news,
    filter_valid_press,
    filter_excluded_news,
    group_and_select_news,
    evaluate_importance,
    AgentState
)
import dotenv
import os
from PIL import Image
import docx
from docx.shared import Pt, RGBColor, Inches
import io
from googlenews import GoogleNews

# 환경 변수 로드
dotenv.load_dotenv()



# 워드 파일 생성 함수
def create_word_document(keyword, filtered_news, analysis):
    # 새 워드 문서 생성
    doc = docx.Document()
    
    # 제목 스타일 설정
    title = doc.add_heading(f'PwC 뉴스 분석 보고서: {keyword}', level=0)
    for run in title.runs:
        run.font.color.rgb = RGBColor(208, 74, 2)  # PwC 오렌지 색상
    
    # 분석 결과 추가
    doc.add_heading('회계법인 관점의 분석 결과', level=1)
    doc.add_paragraph(analysis)
    
    # 선별된 주요 뉴스 추가
    doc.add_heading('선별된 주요 뉴스', level=1)
    
    for i, news in enumerate(filtered_news):
        p = doc.add_paragraph()
        p.add_run(f"{i+1}. {news['content']}").bold = True
        date_str = news.get('date', '날짜 정보 없음')
        date_paragraph = doc.add_paragraph()
        date_paragraph.add_run(f"날짜: {date_str}").italic = True
        doc.add_paragraph(f"출처: {news['url']}")
    
    # 날짜 및 푸터 추가
    current_date = datetime.now().strftime("%Y년 %m월 %d일")
    doc.add_paragraph(f"\n보고서 생성일: {current_date}")
    doc.add_paragraph("© 2024 PwC 뉴스 분석기 | 회계법인 관점의 뉴스 분석 도구")
    
    return doc

# BytesIO 객체로 워드 문서 저장
def get_binary_file_downloader_html(doc, file_name):
    bio = io.BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# 커스텀 CSS
st.markdown("""
<style>
    .title-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .main-title {
        color: #d04a02;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .news-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 4px solid #d04a02;
    }
    .news-title {
        font-weight: 600;
        font-size: 1.1rem;
    }
    .news-url {
        color: #666;
        font-size: 0.9rem;
    }
    .news-date {
        color: #666;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 5px;
    }
    .analysis-box {
        background-color: #f5f5ff;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #d04a02;
    }
    .subtitle {
        color: #dc582a;
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .download-box {
        background-color: #eaf7f0;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #00a36e;
        text-align: center;
    }
    .analysis-section {
        background-color: #f8f9fa;
        border-left: 4px solid #d04a02;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .selected-news {
        border-left: 4px solid #0077b6;
        padding: 15px;
        margin: 10px 0;
        background-color: #f0f8ff;
        border-radius: 5px;
    }
    .excluded-news {
        color: #666;
        padding: 5px 0;
        margin: 5px 0;
        font-size: 0.9em;
    }
    .news-meta {
        color: #666;
        font-size: 0.9em;
        margin: 3px 0;
    }
    .selection-reason {
        color: #666;
        margin: 5px 0;
        font-size: 0.95em;
    }
    .keywords {
        color: #666;
        font-size: 0.9em;
        margin: 5px 0;
    }
    .affiliates {
        color: #666;
        font-size: 0.9em;
        margin: 5px 0;
    }
    .news-url {
        color: #0077b6;
        font-size: 0.9em;
        margin: 5px 0;
        word-break: break-all;
    }
    .news-title-large {
        font-size: 1.2em;
        font-weight: 600;
        color: #000;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    .news-url {
        color: #0077b6;
        font-size: 0.9em;
        margin: 5px 0 10px 0;
        word-break: break-all;
    }
    .news-summary {
        color: #444;
        font-size: 0.95em;
        margin: 10px 0;
        line-height: 1.4;
    }
    .selection-reason {
        color: #666;
        font-size: 0.95em;
        margin: 10px 0;
        line-height: 1.4;
    }
    .importance-high {
        color: #d04a02;
        font-weight: 700;
        margin: 5px 0;
    }
    .importance-medium {
        color: #0077b6;
        font-weight: 700;
        margin: 5px 0;
    }
    .group-indices {
        color: #666;
        font-size: 0.9em;
    }
    .group-selected {
        color: #00a36e;
        font-weight: 600;
    }
    .group-reason {
        color: #666;
        font-size: 0.9em;
        margin-top: 5px;
    }
    .not-selected-news {
        color: #666;
        padding: 5px 0;
        margin: 5px 0;
        font-size: 0.9em;
    }
    .importance-low {
        color: #666;
        font-weight: 700;
        margin: 5px 0;
    }
    .not-selected-reason {
        color: #666;
        margin: 5px 0;
        font-size: 0.95em;
    }
</style>
""", unsafe_allow_html=True)

# 로고와 제목
col1, col2 = st.columns([1, 5])
with col1:
    # 로고 표시
    logo_path = "pwc_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
    else:
        st.error("로고 파일을 찾을 수 없습니다. 프로젝트 루트에 'pwc_logo.png' 파일을 추가해주세요.")

with col2:
    st.markdown("<h1 class='main-title'>PwC 뉴스 분석기</h1>", unsafe_allow_html=True)
    st.markdown("회계법인 관점에서 중요한 뉴스를 자동으로 분석하는 AI 도구")

# 주요 기업 리스트 정의
COMPANIES = ["삼성", "SK", "현대차", "LG", "롯데", "포스코", "한화"]

# 사이드바 설정
st.sidebar.title("🔍 분석 설정")

# 0단계: 기본 설정
st.sidebar.markdown("### 📋 0단계: 기본 설정")

# 유효 언론사 설정
valid_press_dict = st.sidebar.text_area(
    "📰 유효 언론사 설정",
    value="""조선일보: ["조선일보", "chosun", "chosun.com"]
중앙일보: ["중앙일보", "joongang", "joongang.co.kr", "joins.com"]
동아일보: ["동아일보", "donga", "donga.com"]
조선비즈: ["조선비즈", "chosunbiz", "biz.chosun.com"]
한국경제: ["한국경제", "한경", "hankyung", "hankyung.com", "한경닷컴"]
매일경제: ["매일경제", "매경", "mk", "mk.co.kr"]
연합뉴스: ["연합뉴스", "yna", "yna.co.kr"]
파이낸셜뉴스: ["파이낸셜뉴스", "fnnews", "fnnews.com"]
데일리팜: ["데일리팜", "dailypharm", "dailypharm.com"]
IT조선: ["it조선", "it.chosun.com", "itchosun"]
머니투데이: ["머니투데이", "mt", "mt.co.kr"]
비즈니스포스트: ["비즈니스포스트", "businesspost", "businesspost.co.kr"]
이데일리: ["이데일리", "edaily", "edaily.co.kr"]
아시아경제: ["아시아경제", "asiae", "asiae.co.kr"]
뉴스핌: ["뉴스핌", "newspim", "newspim.com"]
뉴시스: ["뉴시스", "newsis", "newsis.com"]
헤럴드경제: ["헤럴드경제", "herald", "heraldcorp", "heraldcorp.com"]""",
    help="분석에 포함할 신뢰할 수 있는 언론사와 그 별칭을 설정하세요. 형식: '언론사: [별칭1, 별칭2, ...]'",
    key="valid_press_dict"
)

# 구분선 추가
st.sidebar.markdown("---")

# 1단계: 제외 판단 기준

# 새로운 기업 추가 섹션
new_company = st.sidebar.text_input(
    "새로운 기업 추가",
    value="",
    help="분석하고 싶은 기업명을 입력하고 Enter를 누르세요. (예: 네이버, 카카오, 현대중공업 등)"
)

# 새로운 기업 추가 로직 수정
if new_company and new_company not in COMPANIES:
    COMPANIES.append(new_company)

# 키워드 선택을 multiselect로 변경
selected_companies = st.sidebar.multiselect(
    "분석할 기업을 선택하세요 (최대 10개)",
    options=COMPANIES,
    default=COMPANIES[:10],  # 처음 10개 기업만 기본 선택으로 설정
    max_selections=10,
    help="분석하고자 하는 기업을 선택하세요. 한 번에 최대 10개까지 선택 가능합니다."
)

# 선택된 키워드를 바로 사용
keywords = selected_companies.copy()

# 구분선 추가
st.sidebar.markdown("---")

# GPT 모델 선택 섹션
st.sidebar.markdown("### 🤖 GPT 모델 선택")

gpt_models = {
    "gpt-4o": "빠르고 실시간, 멀티모달 지원",
    "gpt-4-turbo": "최고 성능, 비용은 좀 있음",
    "gpt-4.1-mini": "성능 높고 비용 저렴, 정밀한 분류·요약에 유리",
    "gpt-4.1-nano": "초고속·초저가, 단순 태그 분류에 적합",
    "gpt-3.5-turbo": "아주 저렴, 간단한 분류 작업에 적당"
}

selected_model = st.sidebar.selectbox(
    "분석에 사용할 GPT 모델을 선택하세요",
    options=list(gpt_models.keys()),
    index=0,  # gpt-4o를 기본값으로 설정
    format_func=lambda x: f"{x} - {gpt_models[x]}",
    help="각 모델의 특성:\n" + "\n".join([f"• {k}: {v}" for k, v in gpt_models.items()])
)

# 모델 설명 표시
st.sidebar.markdown(f"""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; margin-bottom: 20px;'>
    <strong>선택된 모델:</strong> {selected_model}<br>
    <strong>특징:</strong> {gpt_models[selected_model]}
</div>
""", unsafe_allow_html=True)

# 구분선 추가
st.sidebar.markdown("---")

# 검색 결과 수 선택
max_results = st.sidebar.selectbox(
    "검색할 뉴스 수",
    options=[10, 20, 30, 40, 50],
    index=4,  # 기본값을 50으로 설정 (index=4)
    help="검색할 뉴스의 최대 개수를 선택하세요."
)

# 구분선 추가
st.sidebar.markdown("---")

# 시스템 프롬프트 설정
st.sidebar.markdown("### 🤖 시스템 프롬프트")

# 1단계: 제외 판단 시스템 프롬프트
system_prompt_1 = st.sidebar.text_area(
    "1단계: 제외 판단",
    value="당신은 회계법인의 뉴스 분석 전문가입니다. 뉴스의 중요성을 판단하여 제외/보류/유지로 분류하는 작업을 수행합니다. 특히 회계법인의 관점에서 중요하지 않은 뉴스(예: 단순 홍보, CSR 활동, 이벤트 등)를 식별하고, 회계 감리나 재무 관련 이슈는 반드시 유지하도록 합니다.",
    help="1단계 제외 판단에 사용되는 시스템 프롬프트를 설정하세요.",
    key="system_prompt_1",
    height=300
)

# 2단계: 그룹핑 시스템 프롬프트
system_prompt_2 = st.sidebar.text_area(
    "2단계: 그룹핑",
    value="당신은 뉴스 분석 전문가입니다. 유사한 뉴스를 그룹화하고 대표성을 갖춘 기사를 선택하는 작업을 수행합니다. 같은 사안에 대해 숫자, 기업 ,계열사, 맥락, 주요 키워드 등이 유사하면 중복으로 판단합니다. 언론사의 신뢰도와 기사의 상세도를 고려하여 대표 기사를 선정합니다.",
    help="2단계 그룹핑에 사용되는 시스템 프롬프트를 설정하세요.",
    key="system_prompt_2",
    height=300
)

# 3단계: 중요도 평가 시스템 프롬프트
system_prompt_3 = st.sidebar.text_area(
    "3단계: 중요도 평가",
    value="당신은 회계법인의 전문 애널리스트입니다. 뉴스의 중요도를 평가하고 최종 선정하는 작업을 수행합니다. 특히 회계 감리, 재무제표, 경영권 변동, 주요 계약, 법적 분쟁 등 회계법인의 관점에서 중요한 이슈를 식별하고, 그 중요도를 '상' 또는 '중'으로 평가합니다. 또한 각 뉴스의 핵심 키워드와 관련 계열사를 식별하여 보고합니다.",
    help="3단계 중요도 평가에 사용되는 시스템 프롬프트를 설정하세요.",
    key="system_prompt_3",
    height=300
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 1단계: 제외 판단 기준")

# 제외 기준 설정
exclusion_criteria = st.sidebar.text_area(
    "❌ 제외 기준",
    value="""다음 조건 중 하나라도 해당하는 뉴스는 제외하세요:

1. 경기 관련 내용
   - 스포츠단 관련 내용
   - 키워드: 야구단, 축구단, 구단, KBO, 프로야구, 감독, 선수

2. 신제품 홍보, 사회공헌, ESG, 기부 등
   - 키워드: 출시, 기부, 환경 캠페인, 브랜드 홍보, 사회공헌, 나눔, 캠페인 진행, 소비자 반응

3. 단순 시스템 장애, 버그, 서비스 오류
   - 키워드: 일시 중단, 접속 오류, 서비스 오류, 버그, 점검 중, 업데이트 실패

4. 기술 성능, 품질, 테스트 관련 보도
   - 키워드: 우수성 입증, 기술력 인정, 성능 비교, 품질 테스트, 기술 성과""",
    help="분석에서 제외할 뉴스의 기준을 설정하세요.",
    key="exclusion_criteria"
)

# 구분선 추가
st.sidebar.markdown("---")

# 2단계: 그룹핑 기준
st.sidebar.markdown("### 📋 2단계: 그룹핑 기준")

# 중복 처리 기준 설정
duplicate_handling = st.sidebar.text_area(
    "🔄 중복 처리 기준",
    value="""중복 뉴스가 존재할 경우 다음 우선순위로 1개만 선택하십시오:
1. 언론사 우선순위 (높은 순위부터)
   - 1순위: 경제 전문지 (한국경제, 매일경제, 조선비즈, 파이낸셜뉴스)
   - 2순위: 종합 일간지 (조선일보, 중앙일보, 동아일보)
   - 3순위: 통신사 (연합뉴스, 뉴스핌, 뉴시스)
   - 4순위: 기타 언론사

2. 발행 시간 (같은 언론사 내에서)
   - 최신 기사 우선
   - 정확한 시간 정보가 없는 경우, 날짜만 비교

3. 기사 내용의 완성도
   - 더 자세한 정보를 포함한 기사 우선
   - 주요 인용문이나 전문가 의견이 포함된 기사 우선
   - 단순 보도보다 분석적 내용이 포함된 기사 우선

4. 제목의 명확성
   - 더 구체적이고 명확한 제목의 기사 우선
   - 핵심 키워드가 포함된 제목 우선""",
    help="중복된 뉴스를 처리하는 기준을 설정하세요.",
    key="duplicate_handling",
    height=300
)

# 구분선 추가
st.sidebar.markdown("---")

# 3단계: 선택 기준
st.sidebar.markdown("### 📋 3단계: 선택 기준")

# 선택 기준 설정
selection_criteria = st.sidebar.text_area(
    "✅ 선택 기준",
    value="""다음 기준에 해당하는 뉴스가 있다면 반드시 선택해야 합니다:

1. 재무/실적 관련 정보 (최우선 순위)
   - 매출, 영업이익, 순이익 등 실적 발표
   - 재무제표 관련 정보
   - 주가 및 시가총액 변동
   - 배당 정책 변경

2. 회계/감사 관련 정보 (최우선 순위)
   - 회계처리 방식 변경
   - 감사의견 관련 내용
   - 내부회계관리제도
   - 회계 감리 결과
   
3. 구조적 기업가치 변동 정보 (높은 우선순위)
    - 신규사업/투자/계약에 대한 내용
    - 대외 전략(정부 정책, 글로벌 파트너, 지정학 리스크 등)
    - 기업의 새로운 사업전략 및 방향성, 신사업 등
    - 기존 수입모델/사업구조/고객구조 변화
    - 공급망/수요망 등 valuechain 관련 내용 (예: 대형 생산지 이전, 주력 사업군 정리 등) 

4. 기업구조 변경 정보 (높은 우선순위)
   - 인수합병(M&A)
   - 자회사 설립/매각
   - 지분 변동
   - 조직 개편""",
    help="뉴스 선택에 적용할 주요 기준들을 나열하세요.",
    key="selection_criteria",
    height=300
)

# 응답 형식 설정
response_format = st.sidebar.text_area(
    "📝 응답 형식",
    value="""선택된 뉴스 인덱스: [1, 3, 5]와 같은 형식으로 알려주세요.

각 선택된 뉴스에 대해:
제목: (뉴스 제목)
언론사: (언론사명)
발행일: (발행일자)
선정 사유: (구체적인 선정 이유)
분석 키워드: (해당 기업 그룹의 주요 계열사들)

[제외된 주요 뉴스]
제외된 중요 뉴스들에 대해:
인덱스: (뉴스 인덱스)
제목: (뉴스 제목)
제외 사유: (구체적인 제외 이유)""",
    help="분석 결과의 출력 형식을 설정하세요.",
    key="response_format",
    height=200
)

# 최종 프롬프트 생성
analysis_prompt = CUSTOM_PROMPT_TEMPLATE.format(
    selection_criteria=selection_criteria,
    exclusion_criteria=exclusion_criteria,
    valid_press=valid_press_dict,
    duplicate_handling=duplicate_handling
)

# 메인 컨텐츠
if st.button("뉴스 분석 시작", type="primary"):
    for keyword in keywords:
        with st.spinner(f"'{keyword}' 관련 뉴스를 수집하고 분석 중입니다..."):
            # 각 키워드별 상태 초기화
            initial_state = {
                "news_data": [], 
                "filtered_news": [], 
                "analysis": "", 
                "keyword": keyword, 
                "max_results": max_results,
                "model": selected_model,
                "excluded_news": [],
                "borderline_news": [],
                "retained_news": [],
                "grouped_news": [],
                "final_selection": [],
                "exclusion_criteria": exclusion_criteria,
                "duplicate_handling": duplicate_handling,
                "selection_criteria": selection_criteria,
                "system_prompt_1": system_prompt_1,
                "user_prompt_1": "",
                "llm_response_1": "",
                "system_prompt_2": system_prompt_2,
                "user_prompt_2": "",
                "llm_response_2": "",
                "system_prompt_3": system_prompt_3,
                "user_prompt_3": "",
                "llm_response_3": "",
                "not_selected_news": [],
                "original_news_data": []
            }
            
            # 1단계: 뉴스 수집
            st.write("1단계: 뉴스 수집 중...")
            state_after_collection = collect_news(initial_state)
            
            # 2단계: 유효 언론사 필터링
            st.write("2단계: 유효 언론사 필터링 중...")
            state_after_press_filter = filter_valid_press(state_after_collection)
            
            # 3단계: 제외 판단
            st.write("3단계: 제외 판단 중...")
            state_after_exclusion = filter_excluded_news(state_after_press_filter)
            
            # 4단계: 그룹핑
            st.write("4단계: 그룹핑 중...")
            state_after_grouping = group_and_select_news(state_after_exclusion)
            
            # 5단계: 중요도 평가
            st.write("5단계: 중요도 평가 중...")
            final_state = evaluate_importance(state_after_grouping)
            
            # 키워드별 섹션 구분
            st.markdown(f"## 📊 {keyword} 분석 결과")
            
            # 전체 뉴스 표시 (필터링 전)
            with st.expander(f"📰 '{keyword}' 관련 전체 뉴스 (필터링 전)"):
                for i, news in enumerate(final_state.get("original_news_data", []), 1):
                    date_str = news.get('date', '날짜 정보 없음')
                    url = news.get('url', 'URL 정보 없음')
                    press = news.get('press', '알 수 없음')
                    st.markdown(f"""
                    <div class="news-card">
                        <div class="news-title">{i}. {news['content']}</div>
                        <div class="news-meta">📰 {press}</div>
                        <div class="news-date">📅 {date_str}</div>
                        <div class="news-url">🔗 <a href="{url}" target="_blank">{url}</a></div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # 유효 언론사 필터링된 뉴스 표시
            with st.expander(f"📰 '{keyword}' 관련 유효 언론사 뉴스"):
                for i, news in enumerate(final_state["news_data"]):
                    date_str = news.get('date', '날짜 정보 없음')
                    url = news.get('url', 'URL 정보 없음')
                    press = news.get('press', '알 수 없음')
                    st.markdown(f"""
                    <div class="news-card">
                        <div class="news-title">{i+1}. {news['content']}</div>
                        <div class="news-meta">📰 {press}</div>
                        <div class="news-date">📅 {date_str}</div>
                        <div class="news-url">🔗 <a href="{url}" target="_blank">{url}</a></div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # 2단계: 유효 언론사 필터링 결과 표시
            st.markdown("<div class='subtitle'>🔍 2단계: 유효 언론사 필터링 결과</div>", unsafe_allow_html=True)
            st.markdown(f"유효 언론사 뉴스: {len(final_state['news_data'])}개")
            
            # 3단계: 제외/보류/유지 뉴스 표시
            st.markdown("<div class='subtitle'>🔍 3단계: 뉴스 분류 결과</div>", unsafe_allow_html=True)
            
            # 제외된 뉴스
            with st.expander("❌ 제외된 뉴스"):
                for news in final_state["excluded_news"]:
                    st.markdown(f"<div class='excluded-news'>[{news['index']}] {news['title']}<br/>└ {news['reason']}</div>", unsafe_allow_html=True)
            
            # 보류 뉴스
            with st.expander("⚠️ 보류 뉴스"):
                for news in final_state["borderline_news"]:
                    st.markdown(f"<div class='excluded-news'>[{news['index']}] {news['title']}<br/>└ {news['reason']}</div>", unsafe_allow_html=True)
            
            # 유지 뉴스
            with st.expander("✅ 유지 뉴스"):
                for news in final_state["retained_news"]:
                    st.markdown(f"<div class='excluded-news'>[{news['index']}] {news['title']}<br/>└ {news['reason']}</div>", unsafe_allow_html=True)
            
            # 4단계: 그룹핑 결과 표시
            st.markdown("<div class='subtitle'>🔍 4단계: 뉴스 그룹핑 결과</div>", unsafe_allow_html=True)
            
            with st.expander("📋 그룹핑 결과 보기"):
                for group in final_state["grouped_news"]:
                    st.markdown(f"""
                    <div class="analysis-section">
                        <h4>그룹 {group['indices']}</h4>
                        <p>선택된 기사: {group['selected_index']}</p>
                        <p>선정 이유: {group['reason']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # 5단계: 최종 선택 결과 표시
            st.markdown("<div class='subtitle'>🔍 5단계: 최종 선택 결과</div>", unsafe_allow_html=True)
            
            # 선정된 뉴스 표시
            st.markdown("### 📰 최종 선정된 뉴스")
            for news in final_state["final_selection"]:
                # 날짜 형식 변환
                date_str = news.get('date', '')
                #st.write(f"Debug - Original date string: {date_str}")  # 디버그 출력
                
                try:
                    # YYYY-MM-DD 형식으로 가정
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    formatted_date = date_obj.strftime('%m/%d')
                except Exception as e:
                    try:
                        # GMT 형식 시도
                        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
                        formatted_date = date_obj.strftime('%m/%d')
                    except Exception as e:
                        st.write(f"Debug - Date parsing error: {str(e)}")  # 디버그 출력
                        formatted_date = date_str if date_str else '날짜 정보 없음'

                url = news.get('url', 'URL 정보 없음')
                press = news.get('press', '언론사 정보 없음')
                
                st.markdown(f"""
                    <div class="selected-news">
                        <div class="news-title-large">{news['title']} ({formatted_date})</div>
                        <div class="news-url">🔗 <a href="{url}" target="_blank">{url}</a></div>
                        <div class="selection-reason">
                            • 선별 이유: {news['reason']}
                        </div>
                        <div class="news-summary">
                            • 키워드: {', '.join(news['keywords'])} | 관련 계열사: {', '.join(news['affiliates'])} | 언론사: {press}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # 선정되지 않은 뉴스 표시
            if final_state.get("not_selected_news"):
                with st.expander("❌ 선정되지 않은 뉴스"):
                    for news in final_state["not_selected_news"]:
                        st.markdown(f"""
                        <div class="not-selected-news">
                            <div class="news-title">{news['index']}. {news['title']}</div>
                            <div class="importance-low">💡 중요도: {news['importance']}</div>
                            <div class="not-selected-reason">❌ 미선정 사유: {news['reason']}</div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # 워드 파일 다운로드
            st.markdown("<div class='subtitle'>📥 보고서 다운로드</div>", unsafe_allow_html=True)
            doc = create_word_document(keyword, final_state["filtered_news"], final_state["analysis"])
            docx_bytes = get_binary_file_downloader_html(doc, f"PwC_{keyword}_뉴스분석.docx")
            st.download_button(
                label=f"📎 {keyword} 분석 보고서 다운로드",
                data=docx_bytes,
                file_name=f"PwC_{keyword}_뉴스분석.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            
            # 키워드 구분선 추가
            st.markdown("---")
            
            # 디버그 정보
            with st.expander("디버그 정보"):
                st.markdown("### 1단계: 제외 판단")
                st.markdown("#### 시스템 프롬프트")
                st.text(final_state.get("system_prompt_1", "없음"))
                st.markdown("#### 사용자 프롬프트")
                st.text(final_state.get("user_prompt_1", "없음"))
                st.markdown("#### LLM 응답")
                st.text(final_state.get("llm_response_1", "없음"))
                
                st.markdown("### 2단계: 그룹핑")
                st.markdown("#### 시스템 프롬프트")
                st.text(final_state.get("system_prompt_2", "없음"))
                st.markdown("#### 사용자 프롬프트")
                st.text(final_state.get("user_prompt_2", "없음"))
                st.markdown("#### LLM 응답")
                st.text(final_state.get("llm_response_2", "없음"))
                
                st.markdown("### 3단계: 중요도 평가")
                st.markdown("#### 시스템 프롬프트")
                st.text(final_state.get("system_prompt_3", "없음"))
                st.markdown("#### 사용자 프롬프트")
                st.text(final_state.get("user_prompt_3", "없음"))
                st.markdown("#### LLM 응답")
                st.text(final_state.get("llm_response_3", "없음"))
else:
    # 초기 화면 설명
    st.markdown("""
    ### 👋 PwC 뉴스 분석기에 오신 것을 환영합니다!
    
    이 도구는 입력한 키워드에 대한 최신 뉴스를 자동으로 수집하고, 회계법인 관점에서 중요한 뉴스를 선별하여 분석해드립니다.
    
    #### 주요 기능:
    1. 최신 뉴스 자동 수집 (기본 50개)
    2. 3단계 AI 기반 뉴스 분석 프로세스
       - 1단계: 제외/보류/유지 판단
       - 2단계: 유사 뉴스 그룹핑 및 대표 기사 선정
       - 3단계: 중요도 평가 및 최종 선정
    3. 회계법인 관점의 주요 뉴스 선별
    4. 선별된 뉴스에 대한 전문가 분석
    5. 분석 결과 워드 문서로 다운로드
    
    #### 사용 방법:
    1. 사이드바에서 분석할 기업을 선택하세요 (최대 10개)
    2. GPT 모델을 선택하세요 (gpt-4o, gpt-4-turbo 등)
    3. 검색할 뉴스 수를 설정하세요 (10-50개, 기본 50개)
    4. 각 단계별 시스템 프롬프트를 확인/수정하세요
    5. "뉴스 분석 시작" 버튼을 클릭하세요
    
    #### 분석 기준 설정:
    - 제외 기준: 분석에서 제외할 뉴스의 기준
    - 유효 언론사: 신뢰할 수 있는 언론사 목록
    - 중복 처리 기준: 중복 뉴스 처리 우선순위
    - 선택 기준: 중요 뉴스 선정 기준
    - 응답 형식: 분석 결과 출력 형식
    """)

# 푸터
st.markdown("---")
st.markdown("© 2024 PwC 뉴스 분석기 | 회계법인 관점의 뉴스 분석 도구")

def collect_news(state):
    """뉴스를 수집하고 state를 업데이트하는 함수"""
    try:
        # 검색어 설정
        keyword = state.get("keyword", "삼성전자")
        
        # 검색 결과 수 설정
        max_results = state.get("max_results", 50)
        
        # GoogleNews 객체 생성
        news = GoogleNews()
        
        # 뉴스 검색
        news_data = news.search_by_keyword(keyword, k=max_results)
        
        # 수집된 뉴스가 없는 경우
        if not news_data:
            st.error("수집된 뉴스가 없습니다. 다른 키워드로 시도해보세요.")
            return state
        
        # state 업데이트
        state["news_data"] = news_data
        state["filtered_news"] = news_data
        
        # 뉴스 목록 문자열 생성
        news_list = ""
        for news in news_data:
            press = news.get('press', '알 수 없음')
            original_index = news.get('original_index')
            news_list += f"{original_index}. {news['content']} ({press})\n"
        
        return state
        
    except Exception as e:
        st.error(f"뉴스 수집 중 오류가 발생했습니다: {str(e)}")
        return state

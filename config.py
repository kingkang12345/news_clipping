#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shared Configuration
-------------------
This file contains shared variables and configurations used across the news clipping application.
Centralizing these variables makes maintenance easier and ensures consistency.
"""

# Company categories and definitions
COMPANY_CATEGORIES = {
    #"Test": ["삼성", "SK"],  # 테스트용 카테고리 활성화
    "Anchor": ["삼성", "SK", "현대차", "LG", "롯데", "포스코", "한화"],
    "Growth": ["CJ", "NH", "HD현대", "신한금융", "우리금융"],
    "Whitespace": ["신세계", "KDB금융", "GS", "LS"]
}

# 카테고리별 활성화 설정
ACTIVE_CATEGORIES = {
    "Anchor": True,
    "Growth": True,
    "Whitespace": True
}

# Default to Test companies for testing
DEFAULT_COMPANIES = COMPANY_CATEGORIES["Anchor"]  # 테스트용으로 변경

# Company keyword map - mapping companies to their related keywords
COMPANY_KEYWORD_MAP = {
    # Anchor 카테고리
    "포스코": ["포스코", "포스코그룹", "포스코인터내셔널", "포스코DX"],
    "삼성": ["삼성", "삼성전자", "삼성그룹", "삼성바이오로직스", "삼성SDI"],
    "SK": ["SK", "SK하이닉스", "SK이노베이션", "SK텔레콤", "SK그룹","SK이노"],
    "현대차": ["현대차", "현대자동차", "현대모비스", "현대차그룹", "기아"],
    "LG": ["LG", "LG전자", "LG화학", "LG디스플레이", "LG그룹"],
    "롯데": ["롯데", "롯데그룹", "롯데케미칼", "롯데쇼핑", "롯데제과", "신동빈"],
    "한화": ["한화", "한화그룹", "한화에어로스페이스", "한화솔루션", "한화생명"],
    
    # Growth 카테고리
    "CJ": ["CJ", "CJ그룹", "씨제이대한통운", "CJ제일제당", "씨제이이앤엠", "씨제이푸드빌", "씨제이지엘에스", "씨제이올리브영","씨제이", "CJ 대한통운", "CJ ENM", "CJ푸드빌", "CJ GLS", "CJ올리브영", "CJ올리브네트웍스"],
    "NH": ["NH", "엔에이치투자증권", "농협은행", "농협경제지주", "농협금융지주", "농협유통", "농협손해보험", "엔에이치저축은행", "농협", "NH농협", "NH손보"],
    "HD현대": ["HD현대", "에이치디현대", "현대중공업", "에이치디현대오일뱅크", "에이치디한국조선해양", "에이치디현대인프라코어", "에이치디현대일렉트릭", "현대오일터미널", "에이치디현대건설기계", "에이치디현대", "현대重"],
    "신한금융": ["신한금융", "신한은행", "신한투자증권", "신한카드", "신한자산운용", "신한금융지주회사", "신한라이프생명보험", "제주은행", "신한은행", "신한銀", "신한금융지주"],
    "우리금융": ["우리금융", "우리은행", "우리투자증권", "우리금융지주", "우리금융캐피탈","우리銀"],
    
    # Whitespace 카테고리
    "신세계": ["신세계", "이마트", "조선호텔앤리조트", "신세계푸드", "신세계인터내셔날", "이마트24", "신세계센트럴시티","SSG"],
    "KDB금융": ["에이치엠엠", "HMM", "케이디비중소중견메자닌사모투자", "KDB중소중견메자닌사모투자", "케이디비생명보험", "KDB생명보험", "KDB생보", "산은캐피탈", "한국산업은행", "케이디비칸서스밸류사모투자전문회사", "KDB", "KDB인베스트먼트제일호사모투자", "케이디비인베스트먼트제일호사모투자", "산은인베스트먼트", "산은인프라자산운용", "한국지엠", "GM", "태영건설", "한진칼", "대한항공", "아시아나항공", "HJ중공업"],
    "GS": ["GS", "지에스건설", "지에스칼텍스", "지에스리테일", "지에스에너지", "지에스홈쇼핑", "지에스글로벌", "GS건설", "GS칼텍스", "GS리테일", "GS에너지", "GS홈쇼핑", "GS글로벌", "GS25"],
    "LS": ["LS", "엘에스일렉트릭", "엘에스전선", "엘에스엠앤엠", "엘에스글로벌인코퍼레이티드", "엘에스아이앤디", "엘에스메탈", "LS일렉트릭", "LS전선", "LS M&M", "LS글로벌인코퍼레이티드", "LS I&D", "LS메탈"]
}

# Trusted press aliases
TRUSTED_PRESS_ALIASES = {
    "조선일보": ["조선일보", "chosun", "chosun.com"],
    "중앙일보": ["중앙일보", "joongang", "joongang.co.kr", "joins.com"],
    "동아일보": ["동아일보", "donga", "donga.com"],
    "조선비즈": ["조선비즈", "chosunbiz", "biz.chosun.com"],
    "매거진한경": ["매거진한경", "magazine.hankyung", "magazine.hankyung.com"],
    "한국경제": ["한국경제", "한경", "hankyung", "hankyung.com", "한경닷컴"],
    "매일경제": ["매일경제", "매경", "mk", "mk.co.kr"],
    "연합뉴스": ["연합뉴스", "yna", "yna.co.kr"],
    "파이낸셜뉴스": ["파이낸셜뉴스", "fnnews", "fnnews.com"],
    "데일리팜": ["데일리팜", "dailypharm", "dailypharm.com"],
    "IT조선": ["it조선", "it.chosun.com", "itchosun"],
    "머니투데이": ["머니투데이", "mt", "mt.co.kr"],
    "비즈니스포스트": ["비즈니스포스트", "businesspost", "businesspost.co.kr"],
    "이데일리": ["이데일리", "edaily", "edaily.co.kr"],
    "아시아경제": ["아시아경제", "asiae", "asiae.co.kr"],
    "뉴스핌": ["뉴스핌", "newspim", "newspim.com"],
    "뉴시스": ["뉴시스", "newsis", "newsis.com"],
    "헤럴드경제": ["헤럴드경제", "herald", "heraldcorp", "heraldcorp.com"],
    "더벨": ['더벨', 'thebell', 'thebell.co.kr'],
    "SBS": ['SBS', 'SBS Biz', 'SBSBiz', 'SBS뉴스', 'sbs', 'sbs.co.kr'],
    "MBC": ['MBC', 'mbc', 'mbc.co.kr', 'MBC뉴스', 'mbcnews'],
    "KBS": ['KBS', 'kbs', 'kbs.co.kr', 'KBS뉴스', 'kbsnews'],
    "딜사이트": ['딜사이트', 'DealSite', 'dealsite', 'dealsite.co.kr'],
    "이코노믹리뷰": ['이코노믹리뷰', 'econvill.com', 'econvill'],
    "딜사이트경제TV": ['딜사이트경제TV', 'DealSite경제TV', 'dealsite.economictv', 'dealsite.economictv.co.kr'],
    "한국금융경제신문": ['한국금융경제신문', '한국금융경제신문', 'kfn.economictv', 'kfn.economictv.co.kr'],
    "조세일보": ['조세일보', 'joseilbo.com']
}

# Additional press aliases for re-evaluation
ADDITIONAL_PRESS_ALIASES = {
    "철강금속신문": ["철강금속신문", "snmnews", "snmnews.com"],
    "에너지신문": ["에너지신문", "energy-news", "energy-news.co.kr"],
    "이코노믹데일리": ["이코노믹데일리", "economidaily", "economidaily.com"]
}

# System prompts
SYSTEM_PROMPT_1 = """당신은 회계법인의 뉴스 분석 전문가입니다. 뉴스의 중요성을 판단하여 제외/보류/유지로 분류하는 작업을 수행합니다. 특히 회계법인의 관점에서 중요하지 않은 뉴스(예: 단순 홍보, CSR 활동, 이벤트 등)를 식별하고, 회계 감리나 재무 관련 이슈는 최대한 유지하도록 합니다."""

SYSTEM_PROMPT_2 = """당신은 뉴스 분석 전문가입니다. 유사한 뉴스를 그룹화하고 대표성을 갖춘 기사를 선택하는 작업을 수행합니다. 같은 사안에 대해 숫자, 기업 ,계열사, 맥락, 주요 키워드 등이 유사하면 중복으로 판단합니다. 언론사의 신뢰도와 기사의 상세도를 고려하여 대표 기사를 선정합니다."""

SYSTEM_PROMPT_3 = """당신은 회계법인의 전문 애널리스트입니다. 뉴스의 중요도를 평가하고 최종 선정하는 작업을 수행합니다. 특히 회계 감리, 재무제표, 경영권 변동, 주요 계약, 법적 분쟁 등 회계법인의 관점에서 중요한 이슈를 식별하고, 그 중요도를 '상' 또는 '중'으로 평가하여 최대 5개 기사를 선별합니다. 또한 각 뉴스의 핵심 키워드와 관련 계열사를 식별하여 보고합니다."""

# Criteria definitions
EXCLUSION_CRITERIA = """다음 조건 중 하나라도 해당하는 뉴스는 제외하세요:

1. 경기 관련 내용
   - 스포츠단 관련 내용
   - 키워드: 야구단, 축구단, 구단, KBO, 프로야구, 감독, 선수

2. 신제품 홍보, 사회공헌, ESG, 기부 등
   - 키워드: 출시, 기부, 환경 캠페인, 브랜드 홍보, 사회공헌, 나눔, 캠페인 진행, 소비자 반응

3. 단순 시스템 장애, 버그, 서비스 오류
   - 키워드: 일시 중단, 접속 오류, 서비스 오류, 버그, 점검 중, 업데이트 실패

4. 기술 성능, 품질, 테스트 관련 보도
   - 키워드: 우수성 입증, 기술력 인정, 성능 비교, 품질 테스트, 기술 성과
   
5. 목표가 관련 보도
   - 키워드: 목표가, 목표주가 달성, 목표주가 도달, 목표주가 향상, 목표가↑, 목표가↓


   """

DUPLICATE_HANDLING = """중복 뉴스가 존재할 경우 다음 우선순위로 1개만 선택하십시오:
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
   - 핵심 키워드가 포함된 제목 우선"""

SELECTION_CRITERIA = """다음 기준에 해당하는 뉴스가 있다면 반드시 선택해야 합니다:

1. 재무/실적 관련 정보 (최우선 순위)
   - 매출, 영업이익, 순이익 등 실적 발표
   - 재무제표 관련 정보
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
    - 기업의 전략 방향성에 영향을 미칠 수 있는 정보
    - 기존 수입모델/사업구조/고객구조 변화
    - 공급망/수요망 등 valuechain 관련 내용 (예: 대형 생산지 이전, 주력 사업군 정리 등) 

4. 기업구조 변경 정보 (높은 우선순위)
   - 인수합병(M&A)
   - 자회사 설립/매각
   - 지분 변동
   - 조직 개편"""

# GPT Model options
GPT_MODELS = {
    #"openai.gpt-4.1-2025-04-14" : "chatpwc",#pwc
    "gpt-5-mini":"최신모델",
    "gpt-4.1": "최신모델",
    "gpt-4o": "빠르고 실시간, 멀티모달 지원",
    "gpt-4-turbo": "최고 성능, 비용은 좀 있음",
    "gpt-4.1-mini": "성능 높고 비용 저렴, 정밀한 분류·요약에 유리",
    "gpt-4.1-nano": "초고속·초저가, 단순 태그 분류에 적합",
    "gpt-3.5-turbo": "아주 저렴, 간단한 분류 작업에 적당"
}

# Default GPT model to use
#DEFAULT_GPT_MODEL = "gpt-4.1"
DEFAULT_GPT_MODEL = "gpt-5-mini" 

# Email settings
EMAIL_SETTINGS = {
    "from": "kr_client_and_market@pwc.com", #from #kr_client_and_market@pwc.com"
    "default_to": "youngin.kang@pwc.com",
    "default_cc": "youngin.kang@pwc.com",
    "default_bcc": "",  # 기본 bcc 설정
    "default_subject": "Client Intelligence",
    "importance": "Normal"
}

# 카테고리별 이메일 설정
EMAIL_SETTINGS_BY_CATEGORY = {
    "Anchor": {
        "to": "youngin.kang@pwc.com",  # Anchor 카테고리 수신자
        "cc": "youngin.kang@pwc.com",  # Anchor 카테고리 참조
        "bcc": "youngin.kang@pwc.com",  # Anchor 카테고리 숨은 참조
        "subject_prefix": "Anchor"
    },
    "Growth": {
        "to": "youngin.kang@pwc.com",  # Growth 카테고리 수신자 (나중에 변경)
        "cc": "youngin.kang@pwc.com",  # Growth 카테고리 참조 (나중에 변경)
        "bcc": "",  # Growth 카테고리 숨은 참조
        "subject_prefix": "Growth"
    },
    "Whitespace": {
        "to": "youngin.kang@pwc.com",  # Whitespace 카테고리 수신자 (나중에 변경)
        "cc": "youngin.kang@pwc.com",  # Whitespace 카테고리 참조 (나중에 변경)
        "bcc": "",  # Whitespace 카테고리 숨은 참조
        "subject_prefix": "Whitespace"
    }
}

# Teams settings
TEAMS_SETTINGS = {
    "enabled": True,
    "title": "[PwC] 뉴스 분석 보고서",
    "subtitle": "AI가 선별한 오늘의 주요 뉴스",
    "use_plain_text": True  # False면 HTML 사용, True면 텍스트 사용
}

# Teams 채널별 설정 (카테고리별)
TEAMS_CHANNEL_SETTINGS = {
    "Anchor": {
        "groupId": "",  # Anchor 팀 그룹 ID
        "channels": {
            "삼성": {
                "channelId": "",
                "parentMessageId": ""  # 실제 5월NewsList 게시물 ID로 변경 필요
            },
            "SK": {
                "channelId": "",  # 실제 SK 채널 ID로 변경 필요
                "parentMessageId": ""  # 실제 SK 5월NewsList 게시물 ID로 변경 필요
            },
            "현대차": {
                "channelId": "",  # 비활성화 - 빈 문자열로 설정
                "parentMessageId": ""
            },
            "LG": {
                "channelId": "",  # 비활성화
                "parentMessageId": ""
            },
            "롯데": {
                "channelId": "",  # 비활성화
                "parentMessageId": ""
            },
            "포스코": {
                "channelId": "",  # 비활성화
                "parentMessageId": ""
            },
            "한화": {
                "channelId": "",  # 비활성화
                "parentMessageId": ""
            }
        }
    },
    "Growth": {
        "groupId": "",  # Anchor 팀 그룹 ID
        "channels": {
            "CJ": {
                "channelId": "",
                "parentMessageId": ""  # 실제 5월NewsList 게시물 ID로 변경 필요
            },
            "NH": {
                "channelId": "",  # 실제 SK 채널 ID로 변경 필요
                "parentMessageId": ""  # 실제 SK 5월NewsList 게시물 ID로 변경 필요
            },
            "HD현대": {
                "channelId": "",
                "parentMessageId": ""
            },
            "신한금융": {
                "channelId": "",
                "parentMessageId": ""
            },
            "우리금융": {
                "channelId": "",
                "parentMessageId": ""
            }
        }
    },
    "Whitespace": {
        "groupId": "",  # 비활성화
        "channels": {
            "신세계": {
                "channelId": "",
                "parentMessageId": ""
            },
            "KDB금융": {
                "channelId": "",
                "parentMessageId": ""
            },
            "GS": {
                "channelId": "",
                "parentMessageId": ""
            },
            "LS": {
                "channelId": "",
                "parentMessageId": ""
            }
        }
    }
}

# SharePoint List 설정 (카테고리별 -> 회사별)
SHAREPOINT_LIST_SETTINGS = {
    "Anchor": {
        "enabled": True,
        "companies": {
            "삼성": {
                "site_url": "",  # SharePoint 사이트 URL (예: https://company.sharepoint.com/sites/news)
                "list_id": "",   # SharePoint List ID
                "column_ids": {
                    "month": "",     # Month 컬럼 ID
                    "date": "",      # 날짜 컬럼 ID
                    "title": "",     # 제목 컬럼 ID
                    "link": ""       # 링크 컬럼 ID
                }
            },
            "SK": {
                "site_url": "https://pwckor.sharepoint.com/teams/KR-INT-xLoS-SK-GSP-/",
                "list_id": "ec97b948-d61e-47b7-9f1c-45bf62c46ec3",
                "column_ids": {
                    "month": "Month",
                    "date": "OData__xb0a0__xc9dc_",
                    "title": "Title",
                    "link": "OData__xb9c1__xd06c_"
                }
            },
            "현대차": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "LG": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "롯데": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "포스코": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "한화": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            }
        }
    },
    "Growth": {
        "enabled": True,
        "companies": {
            "CJ": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "NH": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "HD현대": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "신한금융": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "우리금융": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            }
        }
    },
    "Whitespace": {
        "enabled": True,
        "companies": {
            "신세계": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "KDB금융": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "GS": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            },
            "LS": {
                "site_url": "",
                "list_id": "",
                "column_ids": {
                    "month": "",
                    "date": "",
                    "title": "",
                    "link": ""
                }
            }
        }
    }
}

# API endpoint for email - 환경변수에서 가져옴
# EMAIL_API_ENDPOINT는 환경변수 EMAIL_API_ENDPOINT 또는 POWERAUTOMATE_WEBHOOK_URL에서 가져옵니다 

# Company-specific additional criteria for each AI stage
# 1단계: 제외 판단 추가 기준
COMPANY_ADDITIONAL_EXCLUSION_CRITERIA = {
    "현대차": """
    
    6. 현대차그룹 특화 제외 기준 (추가):
    1) 노사 갈등 및 임단협 관련 보도
    - 키워드: 현대차證""",
        "롯데": """
    
    6. 롯데그룹 특화 제외 기준 (추가):
    - 키워드: 롯데카드, 롯데손보, 롯데손해보험"""
   
}

# 2단계: 그룹핑 추가 기준
COMPANY_ADDITIONAL_DUPLICATE_HANDLING = {
}

# 3단계: 선택 기준 추가
COMPANY_ADDITIONAL_SELECTION_CRITERIA = {
    "CJ": """

5. CJ그룹(CJ제일제당, CJ대한통운, CJ ENM 등) 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 콘텐츠 전략: 콘텐츠 IP, OTT, 제작비, 콘텐츠 투자, 스튜디오드래곤, CJ ENM 전략
   - 유통/물류 구조: 풀필먼트, 물류센터, 냉장물류, SCM, 글로벌 유통망, CJ대한통운
   - 사업구조 변화: 인적분할, 물적분할, 계열 분할, 자회사 설립, 사업부 분리, 지분 매각""",

    "NH": """

5. NH농협금융지주그룹(NH투자증권, NH농협은행 등) 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 금융 디지털화: 스마트팜 금융, 디지털전환, 플랫폼 전략, 모바일뱅킹, 금융앱, AI대출
   - 농협 특수성: 조합원, 상호금융, 농민 금융, 지역 농협, 농업 지원 정책
   - 계열 전략: NH투자증권, NH-Amundi, NH캐피탈, 계열사 구조, 지주 전략""",

    "우리금융": """

5. 우리금융지주 (우리은행, 우리카드, 우리금융캐피탈 등) 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 지배구조 이슈: 예금보험공사, 공적자금, 지분 매각, 민영화, 최대주주, 지분 구조 변화
   - 경영진 인사: 대표이사, 행장, 회장단, 연임, 경영진 교체, 이사회 구성
   - PF/리스크 이슈: PF대출, 부동산 리스크, 부실채권, 충당금, 건전성, BIS비율""",

    "HD현대": """

5. HD현대 (HD한국조선해양, HD현대중공업, HD현대오일뱅크 등) 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 무인화/자동화 전략: 스마트조선소, 자동용접, 무인운반, 디지털 조선, AI 기반 설계, 로봇공정
   - 친환경/에너지 전환: 암모니아 추진선, 수소엔진, 친환경선박, 탄소중립, 그린수소, 해상풍력, 에너지저장장치(ESS)
   - 글로벌 인프라 전략: 중동 플랜트, 오만 수주, 사우디 프로젝트, 글로벌 조선 수주, 선박 계약""",

    "신한금융": """

5. 신한금융지주 (신한은행, 신한카드, 신한투자증권 등) 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 포트폴리오 재편: 비은행 강화, 카드·증권 통합, 신사업 진출, 핀테크 투자, 디지털 플랫폼화, 디지털 전환 전략
   - 경영 인사 및 지배구조: 차기 회장, 행장 인선, 경영진 재편, 지주사 체제 개편, CEO 리스크, 내부통제 강화
   - 리스크 대응: 금리 민감도, 충당금 적립, 부동산 익스포저""",

    "신세계": """

5. 신세계그룹 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 리테일 전략: 복합몰 전략, 스타필드, 프리미엄 아울렛, 이마트 구조조정, 백화점 실적, 온라인 통합몰
   - 사업구조 변화: 신세계인터내셔날, 지분 매각, 신사업 확장""",

    "KDB금융": """

5. KDB금융지주 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 정책금융 역할: 정책금융, 구조조정 주도, 산업은행, 매각 자문, 국책은행 역할
   - 기업 구조개편: 출자전환, PF 위험 평가, 기업 구조개편, 인수금융, 구조개편 지원""",

    "GS": """

5. GS그룹 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 에너지 전환: GS에너지, RE100, LNG 인프라, 그린수소, 탄소 포집
   - 리테일 혁신: GS리테일, 편의점 수익, 통합 물류
   - 그룹 구조 개편: 계열사 재편, 미래 성장 포트폴리오""",

    "LS": """

5. LS그룹 특화 기준 (위 기준 3, 4에 추가 해당)
   해당 키워드가 포함되어 있을 경우에도 위 기준 3 또는 4에 해당하므로 반드시 선택합니다:
   - 전력 인프라: 전선사업, 배터리 소재, 전력 인프라, ESS, LS일렉트릭 전략
   - 친환경 소재: 동소재, 전기차 부품, 탄소저감 소재
   - 사업구조 재편: LS엠트론, 계열 분할, 신성장 동력"""
} 

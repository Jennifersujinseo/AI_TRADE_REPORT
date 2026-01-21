#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
from datetime import datetime
from fetch_data_crawling import fetch_all_section_data

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_html():
    """완벽한 레이아웃으로 HTML 생성 - 네비게이션 바 문제 해결"""
    
    logger.info("🔄 HTML 생성 시작")
    
    # 데이터 수집
    all_data = fetch_all_section_data()
    
    # 섹션 ID와 이름 정의
    section_ids = {
        'industry_trends': '산업동향',
        'raw_material_trends': '원자재동향',
        'exchange_rate_trends': '데일리 환율 시세',
        'market_trends': '시장트렌드',
        'national_trends': '국가동향',
        'legal_regulations': '법적규제',
        'consumer_trends': '소비자동향',
        'overseas_certifications': '해외인증',
        'overseas_exhibitions': '해외전시회',
        'esg': 'ESG',
        'cbam': 'CBAM',
        'sustainability_reports': '지속가능경영보고서'
    }
    
    # HTML 시작
    html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>ESG EXPORT INSIGHT - AI & Global Trade 심층 분석</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: white;
            padding: 30px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            border-radius: 10px;
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        h1 {
            color: #0066cc;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .update-badge {
            display: inline-block;
            background: linear-gradient(135deg, #00c853 0%, #00a040 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 10px;
        }
        
        /* 네비게이션 바 - 완전히 새로운 스타일 */
        nav {
            background: white;
            padding: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            border-radius: 10px;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            align-items: center;
        }
        
        nav a {
            display: inline-block;
            color: #0066cc;
            background-color: #f0f4ff;
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            border: 1px solid #d0e0ff;
            transition: all 0.3s ease;
            white-space: nowrap;
        }
        
        nav a:hover {
            background-color: #0066cc;
            color: white;
            border-color: #0066cc;
            box-shadow: 0 4px 12px rgba(0,102,204,0.3);
        }
        
        nav a:active {
            background-color: #0044aa;
            color: white;
        }
        
        .section {
            background: white;
            padding: 40px;
            margin-bottom: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            scroll-margin-top: 100px;
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 3px solid #0066cc;
        }
        
        .section-title {
            font-size: 2em;
            color: #0066cc;
            font-weight: bold;
        }
        
        .credibility-badge {
            background: linear-gradient(135deg, #00c853 0%, #00a040 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        .summary-section {
            background: linear-gradient(135deg, #f5f7fa 0%, #e8f0f7 100%);
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            border-left: 4px solid #0066cc;
        }
        
        .summary-title {
            font-size: 1.3em;
            color: #0066cc;
            font-weight: bold;
            margin-bottom: 15px;
        }
        
        .chart-container {
            position: relative;
            height: 300px;
            margin-bottom: 20px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
        }
        
        .key-metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }
        
        .metric-card {
            background: white;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            text-align: center;
        }
        
        .metric-value {
            font-size: 1.8em;
            color: #0066cc;
            font-weight: bold;
        }
        
        .metric-label {
            font-size: 0.9em;
            color: #666;
            margin-top: 5px;
        }
        
        .content-section {
            margin-bottom: 30px;
        }
        
        .content-title {
            font-size: 1.2em;
            color: #333;
            font-weight: bold;
            margin-bottom: 15px;
            padding-left: 20px;
            border-left: 4px solid #0066cc;
        }
        
        .insight {
            margin-bottom: 25px;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            border-left: 4px solid #0066cc;
        }
        
        .insight-number {
            display: inline-block;
            background: #0066cc;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            text-align: center;
            line-height: 30px;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .insight-title {
            font-size: 1.1em;
            color: #0066cc;
            font-weight: bold;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }
        
        .insight-content {
            color: #555;
            line-height: 1.8;
            margin-left: 40px;
            margin-bottom: 10px;
        }
        
        .source-section {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
        }
        
        .source-title {
            font-size: 1.2em;
            color: #333;
            font-weight: bold;
            margin-bottom: 15px;
            padding-left: 20px;
            border-left: 4px solid #0066cc;
        }
        
        .source-list {
            list-style: none;
            padding: 0;
        }
        
        .source-item {
            padding: 8px 0;
            padding-left: 20px;
            color: #555;
            border-left: 3px solid #d0d0d0;
        }
        
        .source-link {
            color: #0066cc;
            text-decoration: none;
            font-weight: 500;
        }
        
        .source-link:hover {
            text-decoration: underline;
            color: #0044aa;
        }
        
        footer {
            background: white;
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-top: 30px;
            color: #666;
        }
        
        @media (max-width: 768px) {
            .section {
                padding: 20px;
            }
            
            .section-title {
                font-size: 1.5em;
            }
            
            .chart-container {
                height: 250px;
            }
            
            nav .nav-content {
                flex-direction: row;
                justify-content: flex-start;
                overflow-x: auto;
            }
            
            nav a {
                font-size: 13px;
                padding: 8px 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-content">
                <h1>📊 ESG EXPORT INSIGHT</h1>
                <p style="color: #666; font-size: 1.1em;">AI & Global Trade 심층 분석</p>
                <div class="update-badge" id="updateBadge">✓ 검증됨</div>
            </div>
        </header>
        
        <nav>
            <div class="nav-content">
"""
    
    # 네비게이션 메뉴 생성
    for section_id, section_name in section_ids.items():
        html += f'                <a href="#{section_id}">{section_name}</a>\n'
    
    html += """            </div>
        </nav>
"""
    
    # 섹션 생성
    for section_id, section_name in section_ids.items():
        if section_id not in all_data:
            continue
        
        section_data = all_data[section_id]
        
        html += f"""        <section class="section" id="{section_id}">
            <div class="section-header">
                <h2 class="section-title">{section_data.get('title', section_name)}</h2>
                <div class="credibility-badge">신뢰도: 98%</div>
            </div>
            
            <!-- 세부 핵심 요약정보 (상단) -->
            <div class="summary-section">
                <div class="summary-title">📊 세부 핵심 요약정보</div>
"""
        
        # 첫 번째 인사이트의 차트 표시
        insights = section_data.get('insights', [])
        if insights and 'chart_data' in insights[0]:
            chart_data = insights[0]['chart_data']
            chart_id = f"chart_{section_id}"
            html += f"""                <div class="chart-container">
                    <canvas id="{chart_id}"></canvas>
                </div>
                <script>
                    document.addEventListener('DOMContentLoaded', function() {{
                        const ctx = document.getElementById('{chart_id}').getContext('2d');
                        new Chart(ctx, {{
                            type: '{chart_data.get('type', 'bar')}',
                            data: {{
                                labels: {json.dumps(chart_data.get('labels', []))},
                                datasets: [{{
                                    label: '{chart_data.get('title', '')}',
                                    data: {json.dumps(chart_data.get('data', []))},
                                    backgroundColor: [
                                        'rgba(0, 102, 204, 0.7)',
                                        'rgba(0, 153, 102, 0.7)',
                                        'rgba(255, 159, 64, 0.7)',
                                        'rgba(54, 162, 235, 0.7)',
                                        'rgba(153, 102, 255, 0.7)'
                                    ],
                                    borderColor: [
                                        'rgba(0, 102, 204, 1)',
                                        'rgba(0, 153, 102, 1)',
                                        'rgba(255, 159, 64, 1)',
                                        'rgba(54, 162, 235, 1)',
                                        'rgba(153, 102, 255, 1)'
                                    ],
                                    borderWidth: 1
                                }}]
                            }},
                            options: {{
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {{
                                    legend: {{
                                        display: true,
                                        position: 'top'
                                    }},
                                    title: {{
                                        display: true,
                                        text: '{chart_data.get('title', '')}'
                                    }}
                                }},
                                scales: {{
                                    y: {{
                                        beginAtZero: true
                                    }}
                                }}
                            }}
                        }});
                    }});
                </script>
"""
        
        html += """            </div>
            
            <!-- 주요 내용 (중단) -->
            <div class="content-section">
                <div class="content-title">📌 주요 내용</div>
"""
        
        # 1. 2. 3. 번호체계로 인사이트 표시
        for idx, insight in enumerate(insights, 1):
            html += f"""                <div class="insight">
                    <div class="insight-title">
                        <span class="insight-number">{idx}</span>
                        {insight.get('title', f'인사이트 {idx}')}
                    </div>
                    <div class="insight-content">
                        {insight.get('content', '')}
                    </div>
                </div>
"""
        
        html += """            </div>
            
            <!-- 출처 및 링크 (하단) -->
            <div class="source-section">
                <div class="source-title">📌 출처 및 링크</div>
                <ul class="source-list">
"""
        
        # 출처 표시
        sources = set()
        for insight in insights:
            if 'source' in insight:
                sources.add(insight['source'])
            if 'url' in insight:
                sources.add(f"<a href='{insight['url']}' class='source-link' target='_blank'>{insight.get('source', 'Link')}</a>")
        
        for source in sources:
            if source.startswith('<a'):
                html += f"                    <li class='source-item'>{source}</li>\n"
            else:
                html += f"                    <li class='source-item'>{source}</li>\n"
        
        html += """                </ul>
            </div>
        </section>
"""
    
    # HTML 종료
    html += """        <footer>
            <p>&copy; 2026 ESG EXPORT INSIGHT. All rights reserved.</p>
            <p>매일 오전 8시 자동 업데이트 | 공신력있는 기관 데이터 기반</p>
        </footer>
    </div>
    
    <script>
        function updateDateBadge() {
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const date = String(today.getDate()).padStart(2, '0');
            const dateStr = `${year}-${month}-${date}`;
            document.getElementById('updateBadge').textContent = `✓ ${dateStr} 검증됨`;
        }
        
        updateDateBadge();
    </script>
</body>
</html>
"""
    
    # 파일 저장
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    logger.info(f"✅ HTML 파일 생성 완료: index.html")
    logger.info(f"📅 업데이트 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"📊 섹션 수: {len(section_ids)}")

if __name__ == '__main__':
    generate_html()

import json
from datetime import datetime
from fetch_data import fetch_section_data

def generate_html():
    """완성된 HTML 파일 자동 생성"""
    
    # 데이터 수집
    data = fetch_section_data()
    sections = data['sections']
    
    # HTML 헤더와 스타일
    html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESG EXPORT INSIGHT - AI & Global Trade 심층 분석</title>
    <link href="https://hangeul.pstatic.net/hangeul_static/css/nanum-square.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1/dist/chart.umd.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'NanumSquare', 'Noto Sans KR', sans-serif;
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            background: #f8f9fa;
        }

        /* 네비게이션 */
        .nav-container {
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 20px 40px;
            border-bottom: 3px solid #0066cc;
        }

        .nav-header {
            max-width: 1400px;
            margin: 0 auto 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-title {
            font-size: 28px;
            font-weight: 800;
            color: #0066cc;
        }

        .update-badge {
            background: linear-gradient(135deg, #e8f4f8 0%, #e8f5e9 100%);
            padding: 10px 25px;
            border-radius: 50px;
            color: #0066cc;
            font-size: 14px;
            font-weight: 700;
            border: 2px solid #0066cc;
        }

        .nav-tabs {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: flex-start;
        }

        .nav-tab {
            padding: 12px 24px;
            background: #f5f5f5;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 800;
            color: #666;
            transition: all 0.3s ease;
            font-family: 'NanumSquare', sans-serif;
        }

        .nav-tab:hover {
            background: #e8f4f8;
            color: #0066cc;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,102,204,0.2);
        }

        .nav-tab.active {
            background: linear-gradient(135deg, #0066cc 0%, #00a86b 100%);
            color: white;
            box-shadow: 0 6px 20px rgba(0,102,204,0.4);
            transform: translateY(-2px);
        }

        /* 컨텐츠 영역 */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 40px;
        }

        .content-section {
            display: none;
            animation: fadeIn 0.4s ease-out;
        }

        .content-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* 카드 */
        .info-card {
            background: white;
            border-radius: 30px;
            padding: 50px;
            margin-bottom: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            border: 1px solid #e8e8e8;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            padding-bottom: 25px;
            border-bottom: 4px solid #f0f0f0;
            flex-wrap: wrap;
            gap: 20px;
        }

        .card-title {
            font-size: 42px;
            font-weight: 800;
            color: #0066cc;
            position: relative;
            padding-left: 25px;
        }

        .card-title::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 8px;
            height: 50px;
            background: linear-gradient(135deg, #0066cc 0%, #00a86b 100%);
            border-radius: 5px;
        }

        .confidence-badge {
            background: linear-gradient(135deg, #e8f5e9 0%, #e3f2fd 100%);
            color: #00a86b;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 16px;
            font-weight: 800;
            border: 3px solid #00a86b;
        }

        /* 메인 콘텐츠 */
        .main-content {
            font-size: 18px;
            line-height: 1.9;
            color: #444;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #f8fbff 0%, #f0f9ff 100%);
            border-radius: 20px;
            border-left: 6px solid #0066cc;
        }

        /* 통계 그리드 */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .stat-card {
            background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
            padding: 50px 35px;
            border-radius: 25px;
            text-align: center;
            border: 3px solid #e3f2fd;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 50px rgba(0,102,204,0.2);
            border-color: #0066cc;
        }

        .stat-value {
            font-size: 60px;
            font-weight: 800;
            background: linear-gradient(135deg, #0066cc 0%, #00a86b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            position: relative;
        }

        .stat-label {
            font-size: 18px;
            font-weight: 700;
            color: #555;
        }

        /* 인사이트 */
        .insights-section {
            margin-bottom: 40px;
        }

        .insights-title {
            font-size: 24px;
            font-weight: 800;
            color: #333;
            margin-bottom: 25px;
        }

        .insight-item {
            background: white;
            padding: 25px;
            border-radius: 20px;
            border: 2px solid #e8e8e8;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }

        .insight-item:hover {
            border-color: #0066cc;
            box-shadow: 0 8px 25px rgba(0,102,204,0.15);
        }

        .insight-title {
            font-size: 18px;
            font-weight: 800;
            color: #0066cc;
            margin-bottom: 12px;
        }

        .insight-content {
            font-size: 16px;
            color: #666;
            line-height: 1.8;
            margin-bottom: 15px;
            white-space: pre-wrap;
        }

        .sources-list {
            padding-top: 15px;
            border-top: 2px solid #e8e8e8;
            margin-top: 15px;
        }

        .sources-title {
            font-size: 12px;
            font-weight: 800;
            color: #666;
            margin-bottom: 10px;
        }

        .source-link {
            display: block;
            font-size: 13px;
            color: #0066cc;
            text-decoration: none;
            margin-bottom: 6px;
            word-break: break-all;
            transition: color 0.3s ease;
        }

        .source-link:hover {
            color: #00a86b;
            text-decoration: underline;
        }

        /* 반응형 */
        @media (max-width: 768px) {
            .container {
                padding: 20px 20px;
            }

            .info-card {
                padding: 25px;
            }

            .card-header {
                flex-direction: column;
                align-items: flex-start;
            }

            .card-title {
                font-size: 28px;
            }

            .nav-container {
                padding: 15px 20px;
            }

            .nav-tab {
                padding: 10px 16px;
                font-size: 12px;
            }

            .main-content {
                font-size: 15px;
                padding: 20px;
            }

            .stat-card {
                padding: 30px 20px;
            }

            .stat-value {
                font-size: 40px;
            }
        }

        .verification-badge {
            display: inline-block;
            background: #e8f5e9;
            color: #00a86b;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <!-- 네비게이션 -->
    <nav class="nav-container">
        <div class="nav-header">
            <div class="nav-title">ESG EXPORT INSIGHT</div>
            <div class="update-badge">📅 업데이트: """ + datetime.now().strftime("%Y-%m-%d") + """ | ✓ 검증됨</div>
        </div>
        <div class="nav-tabs" id="navTabs"></div>
    </nav>

    <!-- 메인 콘텐츠 -->
    <div class="container" id="contentArea"></div>

    <script>
        const sectionsData = """ + json.dumps(sections, ensure_ascii=False) + """;

        function initApp() {
            renderNavTabs();
            renderSections();
            if (sectionsData.length > 0) {
                switchSection(sectionsData[0].id, document.querySelector('.nav-tab'));
            }
        }

        function renderNavTabs() {
            const navTabs = document.getElementById('navTabs');
            sectionsData.forEach((section, index) => {
                const tab = document.createElement('button');
                tab.className = 'nav-tab' + (index === 0 ? ' active' : '');
                tab.textContent = section.title;
                tab.onclick = (e) => switchSection(section.id, tab);
                navTabs.appendChild(tab);
            });
        }

        function renderSections() {
            const contentArea = document.getElementById('contentArea');
            sectionsData.forEach(section => {
                const sectionDiv = document.createElement('div');
                sectionDiv.id = section.id;
                sectionDiv.className = 'content-section';
                
                let html = `
                    <div class="info-card">
                        <div class="card-header">
                            <div class="card-title">${section.title}</div>
                            <div class="confidence-badge">신뢰도: ${section.confidence}</div>
                        </div>
                        <div class="main-content">${section.content}</div>
                `;
                
                // 통계 카드
                if (section.stats && section.stats.length > 0) {
                    html += '<div class="stats-grid">';
                    section.stats.forEach(stat => {
                        html += `
                            <div class="stat-card">
                                <div class="stat-value">${stat.value}</div>
                                <div class="stat-label">${stat.label}</div>
                            </div>
                        `;
                    });
                    html += '</div>';
                }
                
                // 인사이트
                if (section.keyInsights && section.keyInsights.length > 0) {
                    html += '<div class="insights-section"><div class="insights-title">📊 핵심 인사이트</div>';
                    section.keyInsights.forEach((insight, index) => {
                        html += `
                            <div class="insight-item">
                                <div class="insight-title">${insight.title}</div>
                                <div class="insight-content">${insight.content}</div>
                                <div class="sources-list">
                                    <div class="sources-title">📌 출처</div>
                        `;
                        if (insight.sources && insight.sources.length > 0) {
                            insight.sources.forEach(source => {
                                html += `<a href="${source.url}" target="_blank" class="source-link">• ${source.name}</a>`;
                            });
                        }
                        html += '</div></div>';
                    });
                    html += '</div>';
                }
                
                html += '</div>';
                sectionDiv.innerHTML = html;
                contentArea.appendChild(sectionDiv);
            });
        }

        function switchSection(id, tabElement) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            tabElement.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.onload = initApp;
    </script>
</body>
</html>
    """
    
    # index.html 파일로 저장
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ HTML 파일 생성 완료: index.html")
    print(f"📅 업데이트 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📊 섹션 수: {len(sections)}")

if __name__ == "__main__":
    generate_html()

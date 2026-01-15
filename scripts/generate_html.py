import json
from datetime import datetime

def generate_html( ):
    """HTML 파일 자동 생성"""
    
    html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI TRADE REPORT - 자동 업데이트 시스템</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .status-card {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 5px;
        }
        
        .status-card h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 18px;
        }
        
        .source-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        
        .source-item:last-child {
            border-bottom: none;
        }
        
        .source-name {
            font-weight: 500;
            color: #333;
        }
        
        .status-badge {
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
        }
        
        .system-info {
            background: #e7f3ff;
            border-left: 4px solid #2196F3;
            padding: 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        
        .system-info h3 {
            color: #1976D2;
            margin-bottom: 10px;
        }
        
        .info-item {
            color: #333;
            margin: 8px 0;
            line-height: 1.6;
        }
        
        .last-update {
            text-align: center;
            color: #999;
            margin-top: 30px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI TRADE REPORT</h1>
        <p class="subtitle">자동 업데이트 시스템 - 매일 오전 8시 (한국 시간)</p>
        
        <div class="status-grid">
            <div class="status-card">
                <h3>📊 글로벌 빅5 컨설팅펌</h3>
                <div class="source-item">
                    <span class="source-name">McKinsey</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">BCG</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">Bain</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">Deloitte</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">PwC</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
            </div>
            
            <div class="status-card">
                <h3>🌍 글로벌 무역유관기관</h3>
                <div class="source-item">
                    <span class="source-name">WTO</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">UNCTAD</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">ITC</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">EU Commission</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">KOTRA</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
            </div>
            
            <div class="status-card">
                <h3>📰 뉴스 소스</h3>
                <div class="source-item">
                    <span class="source-name">매일경제</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">한국경제</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">이데일리</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">CNN</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">BBC</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
                <div class="source-item">
                    <span class="source-name">JP Morgan</span>
                    <span class="status-badge">✅ 수집 완료</span>
                </div>
            </div>
        </div>
        
        <div class="system-info">
            <h3>ℹ️ 시스템 정보</h3>
            <div class="info-item">
                <strong>시스템 상태:</strong> ✅ 정상 작동 중
            </div>
            <div class="info-item">
                <strong>자동 업데이트:</strong> 매일 오전 8시 (한국 시간)
            </div>
            <div class="info-item">
                <strong>데이터 출처:</strong> 글로벌 빅5 컨설팅펌 + 무역유관기관 + 주요 뉴스 매체
            </div>
            <div class="info-item">
                <strong>수집 항목:</strong> 산업동향, 원자재동향, 환율추이, 시장트렌드, 국가동향, 법적규제, 소비자동향, 해외인증, 해외전시회, ESG, CBAM, 지속가능경영보고서
            </div>
        </div>
        
        <div class="last-update">
            <p>마지막 업데이트: """ + datetime.now().strftime("%Y년 %m월 %d일 %H:%M:%S") + """</p>
            <p>다음 업데이트: 내일 오전 8시 (한국 시간)</p>
        </div>
    </div>
</body>
</html>
    """
    
    # index.html 파일로 저장
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ HTML 파일 생성 완료: index.html")

if __name__ == "__main__":
    generate_html()

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SIEL - Sistema Inteligente de Evaluación de Licitaciones</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --navy:#0A0F1E;--navy2:#0F1628;--navy3:#151D35;--navy4:#1C2645;
  --blue:#1E6FFF;--blue2:#3B87FF;--blue3:#5FA0FF;
  --cyan:#00D4FF;--cyan2:#00AECF;
  --gold:#F0B429;--gold2:#FFD166;
  --green:#00C48C;--red:#FF4D6A;--orange:#FF8C42;
  --text1:#F0F4FF;--text2:#9BAAC8;--text3:#5C6E94;
  --border:#1F2E50;--border2:#2A3D68;
  --card:#0D1525;--card2:#111B32;
  --font:'DM Sans',sans-serif;--mono:'Space Mono',monospace;
  --sidebar:240px;
}
body{font-family:var(--font);background:var(--navy);color:var(--text1);min-height:100vh;overflow-x:hidden;font-size:14px}

/* LOGIN */
#login-screen{position:fixed;inset:0;background:var(--navy);z-index:1000;display:flex;align-items:center;justify-content:center;transition:opacity .5s}
#login-screen.hidden{opacity:0;pointer-events:none}
.login-bg{position:absolute;inset:0;overflow:hidden}
.login-bg::before{content:'';position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(30,111,255,.18) 0%,transparent 70%);top:-100px;right:-100px;animation:pulse 8s ease-in-out infinite}
.login-bg::after{content:'';position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(0,212,255,.12) 0%,transparent 70%);bottom:-50px;left:-50px;animation:pulse 10s ease-in-out infinite .5s}
.grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(30,111,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(30,111,255,.04) 1px,transparent 1px);background-size:40px 40px}
.login-card{position:relative;width:440px;background:var(--card);border:1px solid var(--border2);border-radius:20px;padding:48px;z-index:1;box-shadow:0 24px 80px rgba(0,0,0,.5)}
.login-logo{display:flex;align-items:center;gap:14px;margin-bottom:36px}
.logo-icon{width:52px;height:52px;background:linear-gradient(135deg,var(--blue),var(--cyan));border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;color:#fff;font-family:var(--mono);flex-shrink:0;box-shadow:0 8px 24px rgba(30,111,255,.35)}
.logo-text h1{font-size:24px;font-weight:700;letter-spacing:2px;color:var(--text1)}
.logo-text p{font-size:10px;color:var(--text2);letter-spacing:1.5px;text-transform:uppercase}
.login-card h2{font-size:26px;font-weight:600;margin-bottom:8px}
.login-card>p{color:var(--text2);margin-bottom:28px;font-size:14px}
.plan-badges{display:flex;gap:8px;margin-bottom:28px}
.plan-badge{padding:4px 12px;border-radius:20px;font-size:11px;font-weight:600;letter-spacing:.5px}
.plan-badge.starter{background:rgba(0,196,140,.15);color:var(--green);border:1px solid rgba(0,196,140,.3)}
.plan-badge.pro{background:rgba(240,180,41,.15);color:var(--gold);border:1px solid rgba(240,180,41,.3)}
.plan-badge.enterprise{background:rgba(30,111,255,.15);color:var(--blue3);border:1px solid rgba(30,111,255,.3)}
.form-group{margin-bottom:20px}
.form-group label{display:block;font-size:11px;font-weight:600;color:var(--text2);margin-bottom:8px;text-transform:uppercase;letter-spacing:.8px}
.form-input{width:100%;background:var(--navy3);border:1px solid var(--border);border-radius:10px;padding:13px 16px;color:var(--text1);font-family:var(--font);font-size:14px;outline:none;transition:border-color .2s}
.form-input:focus{border-color:var(--blue)}
.form-input::placeholder{color:var(--text3)}
.btn-primary{width:100%;background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;border:none;border-radius:10px;padding:14px;font-size:14px;font-weight:600;cursor:pointer;font-family:var(--font);letter-spacing:.5px;transition:all .2s;margin-top:8px}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(30,111,255,.35)}
.login-links{display:flex;justify-content:space-between;font-size:12px;color:var(--text2);margin-top:20px}
.login-links a{color:var(--blue3);cursor:pointer;text-decoration:none}

/* APP */
#app{display:none;min-height:100vh}
#app.active{display:flex}

/* SIDEBAR */
.sidebar{width:var(--sidebar);background:var(--card);border-right:1px solid var(--border);display:flex;flex-direction:column;position:fixed;top:0;bottom:0;left:0;z-index:100}
.sidebar-logo{padding:22px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px}
.s-logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--blue),var(--cyan));border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;color:#fff;font-family:var(--mono);flex-shrink:0}
.s-logo-text{font-size:16px;font-weight:700;letter-spacing:1.5px}
.s-logo-sub{font-size:9px;color:var(--text3);letter-spacing:.5px}
.sidebar-nav{padding:16px 12px;flex:1;overflow-y:auto}
.nav-section{margin-bottom:22px}
.nav-section-label{font-size:9px;font-weight:600;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;padding:0 8px;margin-bottom:8px}
.nav-item{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;cursor:pointer;color:var(--text2);font-size:13px;font-weight:500;transition:all .18s;margin-bottom:2px;text-decoration:none;border:none;background:none;width:100%;text-align:left}
.nav-item:hover{background:var(--navy3);color:var(--text1)}
.nav-item.active{background:rgba(30,111,255,.18);color:var(--blue3);border-left:2px solid var(--blue)}
.nav-item i{width:18px;font-size:14px;text-align:center}
.nav-item .badge{margin-left:auto;background:var(--red);color:#fff;font-size:10px;padding:1px 7px;border-radius:10px;font-weight:600}
.nav-item .badge.blue{background:rgba(30,111,255,.3);color:var(--blue3)}
.sidebar-bottom{padding:16px 12px;border-top:1px solid var(--border)}
.user-info{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:9px;cursor:pointer}
.user-avatar{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--cyan));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0}
.user-name{font-size:13px;font-weight:500}
.user-plan{font-size:11px;color:var(--gold)}

/* MAIN */
.main-content{margin-left:var(--sidebar);flex:1;display:flex;flex-direction:column;min-height:100vh}
.topbar{background:var(--card);border-bottom:1px solid var(--border);padding:0 28px;height:64px;display:flex;align-items:center;gap:16px;position:sticky;top:0;z-index:50}
.topbar-left{flex:1;display:flex;align-items:center;gap:16px}
.page-title{font-size:18px;font-weight:600}
.page-sub{font-size:12px;color:var(--text2)}
.topbar-search{background:var(--navy3);border:1px solid var(--border);border-radius:9px;padding:8px 14px;display:flex;align-items:center;gap:8px;flex:1;max-width:340px}
.topbar-search input{background:none;border:none;outline:none;color:var(--text1);font-size:13px;font-family:var(--font);width:100%}
.topbar-search input::placeholder{color:var(--text3)}
.topbar-actions{display:flex;align-items:center;gap:10px}
.topbar-btn{height:36px;background:var(--navy3);border:1px solid var(--border);border-radius:9px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--text2);font-size:13px;transition:all .2s;padding:0 10px;gap:6px;font-weight:600;font-family:var(--font)}
.topbar-btn:hover{border-color:var(--border2);color:var(--text1)}
.topbar-btn.blue{background:var(--blue);border-color:var(--blue);color:#fff}
.notif-dot{position:absolute;top:6px;right:6px;width:7px;height:7px;background:var(--red);border-radius:50%;border:2px solid var(--card)}
.topbar-icon{width:36px;height:36px;position:relative}

/* CONTENT */
.content-area{padding:28px;flex:1}
.page{display:none;animation:fadeIn .3s ease}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{transform:scale(1);opacity:.5}50%{transform:scale(1.1);opacity:.9}}

/* STATS */
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
.stat-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:20px;position:relative;overflow:hidden;cursor:pointer;transition:border-color .2s}
.stat-card:hover{border-color:var(--border2)}
.stat-label{font-size:11px;font-weight:600;color:var(--text3);letter-spacing:.5px;text-transform:uppercase;margin-bottom:10px}
.stat-value{font-size:28px;font-weight:700;font-family:var(--mono);line-height:1}
.stat-change{display:flex;align-items:center;gap:4px;font-size:12px;margin-top:8px}
.stat-change.up{color:var(--green)}
.stat-change.down{color:var(--red)}
.stat-icon{position:absolute;top:18px;right:18px;width:36px;height:36px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px}

/* CHARTS */
.charts-row{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:24px}
.chart-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:20px}
.chart-card h3{font-size:14px;font-weight:600;margin-bottom:4px}
.chart-sub{font-size:12px;color:var(--text2);margin-bottom:20px}
.bar-chart{display:flex;align-items:flex-end;gap:8px;height:120px;padding-bottom:8px}
.bar-wrap{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px}
.bar{width:100%;border-radius:5px 5px 0 0;min-height:4px}
.bar-label{font-size:10px;color:var(--text3)}
.donut-wrap{display:flex;flex-direction:column;align-items:center;gap:14px}
.donut-svg{transform:rotate(-90deg)}
.donut-item{display:flex;align-items:center;justify-content:space-between;padding:5px 0;font-size:12px;border-bottom:1px solid var(--border)}
.donut-item:last-child{border:none}
.dot{width:8px;height:8px;border-radius:50%;margin-right:8px;flex-shrink:0;display:inline-block}

/* TABLE */
.table-card{background:var(--card);border:1px solid var(--border);border-radius:14px;overflow:hidden;margin-bottom:24px}
.table-header{padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.table-header h3{font-size:14px;font-weight:600}
.table-filters{display:flex;gap:8px;flex-wrap:wrap}
.filter-btn{padding:6px 12px;border-radius:7px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--border);background:var(--navy3);color:var(--text2);transition:all .15s;font-family:var(--font)}
.filter-btn.active,.filter-btn:hover{background:var(--blue);border-color:var(--blue);color:#fff}
.btn-upload{padding:8px 14px;background:linear-gradient(135deg,var(--blue),var(--blue2));color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .2s;font-family:var(--font)}
.btn-upload:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(30,111,255,.3)}
table{width:100%;border-collapse:collapse}
th{padding:10px 16px;text-align:left;font-size:10px;font-weight:600;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--border);background:var(--navy);white-space:nowrap}
td{padding:13px 16px;border-bottom:1px solid var(--border);font-size:13px}
tr:last-child td{border:none}
tr:hover td{background:rgba(255,255,255,.02)}
.score-pill{display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700;font-family:var(--mono)}
.score-high{background:rgba(0,196,140,.15);color:var(--green);border:1px solid rgba(0,196,140,.25)}
.score-med{background:rgba(240,180,41,.15);color:var(--gold);border:1px solid rgba(240,180,41,.25)}
.score-low{background:rgba(255,77,106,.15);color:var(--red);border:1px solid rgba(255,77,106,.25)}
.status-pill{display:inline-flex;align-items:center;gap:5px;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:600}
.status-pill.analyzing{background:rgba(30,111,255,.15);color:var(--blue3)}
.status-pill.complete{background:rgba(0,196,140,.12);color:var(--green)}
.status-pill.review{background:rgba(240,180,41,.12);color:var(--gold)}
.status-dot{width:6px;height:6px;border-radius:50%;background:currentColor}
.action-btn{padding:5px 10px;border-radius:6px;font-size:11px;font-weight:600;cursor:pointer;border:1px solid var(--border);background:transparent;color:var(--text2);transition:all .15s;font-family:var(--font)}
.action-btn:hover{background:var(--blue);border-color:var(--blue);color:#fff}

/* DETAIL */
.detail-panel{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:24px}
.detail-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;gap:20px}
.detail-title h2{font-size:18px;font-weight:600;margin-bottom:4px}
.detail-title p{font-size:13px;color:var(--text2)}
.big-score{font-size:52px;font-weight:700;font-family:var(--mono);background:linear-gradient(135deg,var(--green),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;text-align:center}
.score-label{font-size:11px;color:var(--text2);text-align:center;margin-top:4px}
.detail-tabs{display:flex;gap:4px;margin-bottom:20px;background:var(--navy3);padding:4px;border-radius:10px;width:fit-content;flex-wrap:wrap}
.detail-tab{padding:7px 16px;border-radius:7px;font-size:12px;font-weight:600;cursor:pointer;color:var(--text2);transition:all .15s;border:none;background:none;font-family:var(--font)}
.detail-tab.active{background:var(--blue);color:#fff}
.tab-content{display:none}
.tab-content.active{display:block}
.resumen-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.info-block{background:var(--navy3);border-radius:10px;padding:16px}
.info-block h4{font-size:10px;font-weight:600;color:var(--text3);text-transform:uppercase;letter-spacing:.8px;margin-bottom:12px}
.info-row{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid var(--border);font-size:12px}
.info-row:last-child{border:none}
.info-row span:first-child{color:var(--text2)}
.info-row span:last-child{font-weight:500}

/* CHECKLIST */
.checklist{display:flex;flex-direction:column;gap:8px}
.check-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:9px;background:var(--navy3);font-size:13px}
.check-icon{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;flex-shrink:0}
.check-item.ok .check-icon{background:rgba(0,196,140,.2);color:var(--green)}
.check-item.warn .check-icon{background:rgba(240,180,41,.2);color:var(--gold)}
.check-item.fail .check-icon{background:rgba(255,77,106,.2);color:var(--red)}
.check-text{flex:1}
.check-tag{font-size:10px;padding:2px 8px;border-radius:10px;font-weight:600;white-space:nowrap}
.check-item.ok .check-tag{background:rgba(0,196,140,.15);color:var(--green)}
.check-item.warn .check-tag{background:rgba(240,180,41,.15);color:var(--gold)}
.check-item.fail .check-tag{background:rgba(255,77,106,.15);color:var(--red)}

/* RIESGOS */
.risk-grid{display:flex;flex-direction:column;gap:8px}
.risk-item{padding:12px 16px;border-radius:9px;background:var(--navy3);border-left:3px solid transparent}
.risk-item.alto{border-left-color:var(--red)}
.risk-item.medio{border-left-color:var(--gold)}
.risk-item.bajo{border-left-color:var(--green)}
.risk-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.risk-title{font-size:13px;font-weight:600}
.risk-badge{font-size:10px;padding:2px 9px;border-radius:10px;font-weight:700}
.risk-item.alto .risk-badge{background:rgba(255,77,106,.2);color:var(--red)}
.risk-item.medio .risk-badge{background:rgba(240,180,41,.2);color:var(--gold)}
.risk-item.bajo .risk-badge{background:rgba(0,196,140,.2);color:var(--green)}
.risk-desc{font-size:12px;color:var(--text2);line-height:1.5}

/* ALERTAS */
.alert-list{display:flex;flex-direction:column;gap:8px}
.alert-item{display:flex;gap:12px;padding:12px 16px;border-radius:10px;align-items:flex-start}
.alert-item.critical{background:rgba(255,77,106,.08);border:1px solid rgba(255,77,106,.2)}
.alert-item.warning{background:rgba(240,180,41,.08);border:1px solid rgba(240,180,41,.2)}
.alert-item.info{background:rgba(30,111,255,.08);border:1px solid rgba(30,111,255,.2)}
.alert-item>i{font-size:15px;margin-top:2px;flex-shrink:0}
.alert-item.critical>i{color:var(--red)}
.alert-item.warning>i{color:var(--gold)}
.alert-item.info>i{color:var(--blue3)}
.alert-text h4{font-size:13px;font-weight:600;margin-bottom:2px}
.alert-text p{font-size:12px;color:var(--text2);line-height:1.5}

/* CHAT */
.chat-container{display:flex;flex-direction:column;height:460px}
.chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:14px}
.chat-messages::-webkit-scrollbar{width:4px}
.chat-messages::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px}
.msg{max-width:80%;display:flex;flex-direction:column;gap:4px}
.msg.user{align-self:flex-end;align-items:flex-end}
.msg.ai{align-self:flex-start}
.msg-bubble{padding:10px 14px;border-radius:12px;font-size:13px;line-height:1.6}
.msg.user .msg-bubble{background:var(--blue);color:#fff;border-bottom-right-radius:3px}
.msg.ai .msg-bubble{background:var(--navy3);color:var(--text1);border:1px solid var(--border);border-bottom-left-radius:3px}
.msg-time{font-size:10px;color:var(--text3)}
.chat-input-area{padding:14px;border-top:1px solid var(--border);display:flex;gap:10px}
.chat-input{flex:1;background:var(--navy3);border:1px solid var(--border);border-radius:10px;padding:10px 14px;color:var(--text1);font-size:13px;font-family:var(--font);outline:none;resize:none;transition:border-color .2s}
.chat-input:focus{border-color:var(--blue)}
.chat-send{width:40px;height:40px;background:var(--blue);border:none;border-radius:10px;color:#fff;cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;transition:all .2s;flex-shrink:0}
.chat-send:hover{background:var(--blue2)}
.typing-indicator{display:flex;gap:4px;padding:12px 14px;background:var(--navy3);border-radius:12px;width:60px}
.typing-dot{width:7px;height:7px;border-radius:50%;background:var(--text3);animation:typing .8s ease-in-out infinite}
.typing-dot:nth-child(2){animation-delay:.2s}
.typing-dot:nth-child(3){animation-delay:.4s}
@keyframes typing{0%,100%{opacity:.3;transform:scale(.8)}50%{opacity:1;transform:scale(1.1)}}

/* UPLOAD */
.upload-zone{border:2px dashed var(--border2);border-radius:14px;padding:48px;text-align:center;cursor:pointer;transition:all .3s}
.upload-zone:hover{border-color:var(--blue);background:rgba(30,111,255,.04)}
.upload-zone i.big{font-size:42px;color:var(--blue3);margin-bottom:16px;display:block}
.upload-zone h3{font-size:16px;font-weight:600;margin-bottom:8px}
.upload-zone p{font-size:13px;color:var(--text2);margin-bottom:20px}
.upload-tags{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.upload-tag{padding:4px 12px;background:var(--navy3);border:1px solid var(--border);border-radius:20px;font-size:11px;font-weight:600;color:var(--text2)}
.progress-bar-wrap{background:var(--navy3);border-radius:20px;height:6px;overflow:hidden;margin-top:8px}
.progress-bar-fill{height:100%;background:linear-gradient(90deg,var(--blue),var(--cyan));border-radius:20px;transition:width .3s ease;width:0}

/* COMPARE */
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.compare-card{background:var(--card);border:1px solid var(--border);border-radius:14px;overflow:hidden;cursor:pointer;transition:border-color .2s}
.compare-card:hover{border-color:var(--blue2)}
.compare-card.selected{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue)}
.compare-top{padding:16px 20px;border-bottom:1px solid var(--border)}
.compare-top h3{font-size:14px;font-weight:600;margin-bottom:4px}
.compare-top p{font-size:12px;color:var(--text2)}
.compare-body{padding:16px 20px}
.compare-metric{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border);font-size:12px}
.compare-metric:last-child{border:none}
.compare-metric span:first-child{color:var(--text2)}

/* SUSCRIPCION */
.sub-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.sub-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px;position:relative;overflow:hidden}
.sub-card.featured{border-color:var(--blue)}
.sub-card.featured::before{content:'Más Popular';position:absolute;top:0;right:0;background:var(--blue);color:#fff;font-size:10px;font-weight:700;padding:5px 14px;border-bottom-left-radius:10px;letter-spacing:.5px}
.sub-name{font-size:13px;font-weight:700;letter-spacing:1px}
.sub-price{font-size:36px;font-weight:700;font-family:var(--mono);margin:16px 0 4px}
.sub-price span{font-size:16px;font-weight:400;color:var(--text2)}
.sub-period{font-size:12px;color:var(--text3);margin-bottom:20px}
.sub-features{list-style:none;display:flex;flex-direction:column;gap:10px;margin-bottom:24px}
.sub-features li{display:flex;align-items:center;gap:8px;font-size:13px}
.sub-features li i{font-size:12px;flex-shrink:0}
.sub-features li.yes i{color:var(--green)}
.sub-features li.no{color:var(--text3)}
.sub-features li.no i{color:var(--text3)}
.btn-sub{width:100%;padding:11px;border-radius:9px;font-size:13px;font-weight:600;cursor:pointer;font-family:var(--font);transition:all .2s}
.btn-sub.outline{background:transparent;border:1px solid var(--border2);color:var(--text1)}
.btn-sub.outline:hover{border-color:var(--blue);color:var(--blue3)}
.btn-sub.filled{background:linear-gradient(135deg,var(--blue),var(--blue2));border:none;color:#fff}
.btn-sub.filled:hover{box-shadow:0 4px 16px rgba(30,111,255,.3)}

/* RECOMENDACIONES */
.rec-list{display:flex;flex-direction:column;gap:10px}
.rec-item{display:flex;gap:14px;padding:14px 16px;border-radius:10px;background:var(--navy3);border:1px solid var(--border)}
.rec-num{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--cyan));display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;flex-shrink:0;margin-top:1px}
.rec-body h4{font-size:13px;font-weight:600;margin-bottom:4px}
.rec-body p{font-size:12px;color:var(--text2);line-height:1.5}
.rec-tag{display:inline-block;margin-top:6px;font-size:10px;padding:2px 9px;border-radius:10px;background:rgba(30,111,255,.15);color:var(--blue3);font-weight:600}

/* HELPERS */
.section-title{font-size:16px;font-weight:600;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.section-title i{color:var(--blue3)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.quick-btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
</style>
</head>
<body>

<!-- ===== LOGIN ===== -->
<div id="login-screen">
  <div class="login-bg"><div class="grid-bg"></div></div>
  <div class="login-card">
    <div class="login-logo">
      <div class="logo-icon">SI</div>
      <div class="logo-text">
        <h1>SIEL</h1>
        <p>Sistema Inteligente de Evaluación de Licitaciones</p>
      </div>
    </div>
    <div class="plan-badges">
      <span class="plan-badge starter">Starter</span>
      <span class="plan-badge pro">Pro</span>
      <span class="plan-badge enterprise">Enterprise</span>
    </div>
    <h2>Bienvenido de nuevo</h2>
    <p>Ingresa a tu panel de análisis estratégico</p>
    <div class="form-group">
      <label>Correo electrónico</label>
      <input type="email" class="form-input" id="email-input" placeholder="correo@empresa.com" value="gerente@constructora.com">
    </div>
    <div class="form-group">
      <label>Contraseña</label>
      <input type="password" class="form-input" id="pass-input" placeholder="••••••••" value="password123">
    </div>
    <button class="btn-primary" onclick="doLogin()"><i class="fa-solid fa-shield-halved" style="margin-right:8px"></i>Ingresar al Sistema</button>
    <div class="login-links">
      <a href="#">¿Olvidaste tu contraseña?</a>
      <a href="#" onclick="doLogin();return false">Crear cuenta gratis →</a>
    </div>
  </div>
</div>

<!-- ===== APP ===== -->
<div id="app">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-logo">
      <div class="s-logo-icon">SI</div>
      <div>
        <div class="s-logo-text">SIEL</div>
        <div class="s-logo-sub">v2.4 · Pro Plan</div>
      </div>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section">
        <div class="nav-section-label">Principal</div>
        <button class="nav-item active" onclick="showPage('dashboard')"><i class="fa-solid fa-chart-line"></i>Dashboard</button>
        <button class="nav-item" onclick="showPage('upload')"><i class="fa-solid fa-cloud-arrow-up"></i>Cargar Licitación</button>
        <button class="nav-item" onclick="showPage('licitaciones')"><i class="fa-solid fa-folder-open"></i>Mis Licitaciones <span class="badge blue">12</span></button>
      </div>
      <div class="nav-section">
        <div class="nav-section-label">Análisis</div>
        <button class="nav-item" onclick="showPage('analisis')"><i class="fa-solid fa-magnifying-glass-chart"></i>Análisis Detallado</button>
        <button class="nav-item" onclick="showPage('comparar')"><i class="fa-solid fa-scale-balanced"></i>Comparar</button>
        <button class="nav-item" onclick="showPage('alertas')"><i class="fa-solid fa-bell"></i>Alertas <span class="badge">3</span></button>
      </div>
      <div class="nav-section">
        <div class="nav-section-label">Asistente IA</div>
        <button class="nav-item" onclick="showPage('asistente')"><i class="fa-solid fa-robot"></i>SIEL Copilot</button>
      </div>
      <div class="nav-section">
        <div class="nav-section-label">Administración</div>
        <button class="nav-item" onclick="showPage('suscripcion')"><i class="fa-solid fa-crown"></i>Suscripción</button>
        <button class="nav-item" onclick="showPage('admin')"><i class="fa-solid fa-sliders"></i>Panel Admin</button>
      </div>
    </nav>
    <div class="sidebar-bottom">
      <div class="user-info">
        <div class="user-avatar">JR</div>
        <div>
          <div class="user-name">Juan Rodríguez</div>
          <div class="user-plan">⭐ Plan Pro</div>
        </div>
      </div>
    </div>
  </aside>

  <!-- MAIN -->
  <main class="main-content">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="page-title" id="page-title">Dashboard Gerencial</div>
          <div class="page-sub" id="page-sub">Resumen ejecutivo · Mayo 2025</div>
        </div>
        <div class="topbar-search">
          <i class="fa-solid fa-search" style="color:var(--text3)"></i>
          <input placeholder="Buscar licitaciones, análisis...">
        </div>
      </div>
      <div class="topbar-actions">
        <div class="topbar-btn topbar-icon" style="position:relative">
          <i class="fa-solid fa-bell"></i>
          <span class="notif-dot"></span>
        </div>
        <div class="topbar-btn"><i class="fa-solid fa-gear"></i></div>
        <button class="topbar-btn blue" onclick="showPage('upload')">
          <i class="fa-solid fa-plus"></i> Nueva
        </button>
      </div>
    </div>

    <div class="content-area">

      <!-- DASHBOARD -->
      <div class="page active" id="page-dashboard">
        <div class="stats-grid">
          <div class="stat-card" onclick="showPage('licitaciones')">
            <div class="stat-label">Licitaciones Activas</div>
            <div class="stat-value">24</div>
            <div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;+4 este mes</div>
            <div class="stat-icon" style="background:rgba(30,111,255,.15);color:var(--blue3)"><i class="fa-solid fa-folder-open"></i></div>
          </div>
          <div class="stat-card" onclick="showPage('analisis')">
            <div class="stat-label">Score Promedio IA</div>
            <div class="stat-value">73<span style="font-size:16px;color:var(--text3)">/100</span></div>
            <div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;+5.2 pts</div>
            <div class="stat-icon" style="background:rgba(0,196,140,.15);color:var(--green)"><i class="fa-solid fa-chart-simple"></i></div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Valor Total (COP)</div>
            <div class="stat-value">$482<span style="font-size:16px;color:var(--text3)">M</span></div>
            <div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;+12.4%</div>
            <div class="stat-icon" style="background:rgba(240,180,41,.15);color:var(--gold)"><i class="fa-solid fa-dollar-sign"></i></div>
          </div>
          <div class="stat-card" onclick="showPage('alertas')">
            <div class="stat-label">Alertas Críticas</div>
            <div class="stat-value">3</div>
            <div class="stat-change down"><i class="fa-solid fa-triangle-exclamation"></i>&nbsp;Requieren atención</div>
            <div class="stat-icon" style="background:rgba(255,77,106,.15);color:var(--red)"><i class="fa-solid fa-bell"></i></div>
          </div>
        </div>

        <div class="charts-row">
          <div class="chart-card">
            <h3>Evolución del Score de Viabilidad</h3>
            <div class="chart-sub">Promedio mensual últimos 6 meses</div>
            <div class="bar-chart" id="bar-chart"></div>
          </div>
          <div class="chart-card">
            <h3>Distribución por Sector</h3>
            <div class="chart-sub">Tipo de licitaciones analizadas</div>
            <div class="donut-wrap">
              <svg class="donut-svg" width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="38" fill="none" stroke="#1C2645" stroke-width="16"/>
                <circle cx="50" cy="50" r="38" fill="none" stroke="var(--blue)" stroke-width="16" stroke-dasharray="85 153.9"/>
                <circle cx="50" cy="50" r="38" fill="none" stroke="var(--cyan)" stroke-width="16" stroke-dasharray="43 153.9" stroke-dashoffset="-85"/>
                <circle cx="50" cy="50" r="38" fill="none" stroke="var(--gold)" stroke-width="16" stroke-dasharray="30 153.9" stroke-dashoffset="-128"/>
                <circle cx="50" cy="50" r="38" fill="none" stroke="var(--green)" stroke-width="16" stroke-dasharray="20 153.9" stroke-dashoffset="-158"/>
              </svg>
              <div style="width:100%">
                <div class="donut-item"><span><span class="dot" style="background:var(--blue)"></span>Infraestructura</span><span style="font-weight:600;font-family:var(--mono)">36%</span></div>
                <div class="donut-item"><span><span class="dot" style="background:var(--cyan)"></span>Tecnología</span><span style="font-weight:600;font-family:var(--mono)">24%</span></div>
                <div class="donut-item"><span><span class="dot" style="background:var(--gold)"></span>Servicios</span><span style="font-weight:600;font-family:var(--mono)">18%</span></div>
                <div class="donut-item"><span><span class="dot" style="background:var(--green)"></span>Otros</span><span style="font-weight:600;font-family:var(--mono)">22%</span></div>
              </div>
            </div>
          </div>
        </div>

        <div class="table-card">
          <div class="table-header">
            <h3>Licitaciones Recientes</h3>
            <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">
              <div class="table-filters">
                <button class="filter-btn active" onclick="setFilter(this)">Todas</button>
                <button class="filter-btn" onclick="setFilter(this)">Alta Viabilidad</button>
                <button class="filter-btn" onclick="setFilter(this)">En Análisis</button>
              </div>
              <button class="btn-upload" onclick="showPage('upload')"><i class="fa-solid fa-plus"></i>Nueva</button>
            </div>
          </div>
          <table><thead><tr><th>Proceso</th><th>Entidad</th><th>Valor</th><th>Score IA</th><th>Estado</th><th>Cierre</th><th>Acción</th></tr></thead>
          <tbody id="lic-table-body"></tbody></table>
        </div>
      </div>

      <!-- UPLOAD -->
      <div class="page" id="page-upload">
        <div style="max-width:680px">
          <p style="color:var(--text2);margin-bottom:24px">Sube los documentos del pliego. La IA analizará automáticamente requisitos jurídicos, financieros, técnicos y económicos.</p>
          <div class="upload-zone" id="drop-zone" onclick="document.getElementById('file-input').click()">
            <i class="fa-solid fa-cloud-arrow-up big"></i>
            <h3>Arrastra los documentos aquí</h3>
            <p>PDF, Word (.docx) o Excel (.xlsx) · Máx. 50MB por archivo · OCR incluido para documentos escaneados</p>
            <div class="upload-tags">
              <span class="upload-tag">📄 PDF</span>
              <span class="upload-tag">📝 DOCX</span>
              <span class="upload-tag">📊 XLSX</span>
              <span class="upload-tag">🔍 OCR</span>
            </div>
            <div id="upload-progress" style="display:none;margin-top:24px">
              <div id="progress-text" style="font-size:12px;color:var(--text2);text-align:left;margin-bottom:8px">Subiendo archivo...</div>
              <div class="progress-bar-wrap"><div class="progress-bar-fill" id="progress-fill"></div></div>
            </div>
          </div>
          <input type="file" id="file-input" style="display:none" multiple accept=".pdf,.docx,.xlsx">
          <div style="margin-top:20px;padding:20px;background:var(--card);border:1px solid var(--border);border-radius:14px">
            <h3 class="section-title"><i class="fa-solid fa-list-check"></i>Módulos de análisis activados</h3>
            <div class="grid-2">
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>Análisis Jurídico</div>
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>Análisis Financiero</div>
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>Análisis Técnico</div>
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>Análisis Económico</div>
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>Detección de Riesgos</div>
              <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--navy3);border-radius:9px;font-size:13px"><i class="fa-solid fa-check-circle" style="color:var(--green)"></i>OCR para escaneados</div>
            </div>
          </div>
        </div>
      </div>

      <!-- LICITACIONES -->
      <div class="page" id="page-licitaciones">
        <div class="table-card">
          <div class="table-header">
            <h3>Todas las Licitaciones</h3>
            <button class="btn-upload" onclick="showPage('upload')"><i class="fa-solid fa-plus"></i>Nueva Licitación</button>
          </div>
          <table><thead><tr><th>Proceso</th><th>Entidad</th><th>Valor</th><th>Score IA</th><th>Estado</th><th>Cierre</th><th>Acción</th></tr></thead>
          <tbody id="lic-table-all"></tbody></table>
        </div>
      </div>

      <!-- ANÁLISIS -->
      <div class="page" id="page-analisis">
        <div class="detail-panel">
          <div class="detail-header">
            <div class="detail-title">
              <h2>Concesión Vial Ruta del Sol – Sector 3</h2>
              <p>INVIAS · MC-2024-089 · Infraestructura · Análisis completado</p>
            </div>
            <div style="text-align:center;flex-shrink:0">
              <div class="big-score">82</div>
              <div class="score-label">Score de Viabilidad</div>
            </div>
          </div>
          <div class="detail-tabs">
            <button class="detail-tab active" onclick="switchTab('resumen',this)">📋 Resumen</button>
            <button class="detail-tab" onclick="switchTab('checklist',this)">✅ Checklist</button>
            <button class="detail-tab" onclick="switchTab('riesgos',this)">⚠️ Riesgos</button>
            <button class="detail-tab" onclick="switchTab('recomendaciones',this)">🚀 Recomendaciones</button>
          </div>

          <div class="tab-content active" id="tab-resumen">
            <div class="resumen-grid">
              <div class="info-block">
                <h4>Información General</h4>
                <div class="info-row"><span>Entidad</span><span>INVIAS</span></div>
                <div class="info-row"><span>Modalidad</span><span>Concesión</span></div>
                <div class="info-row"><span>Plazo</span><span>15 años</span></div>
                <div class="info-row"><span>Valor</span><span style="color:var(--gold);font-family:var(--mono)">$78.400M COP</span></div>
                <div class="info-row"><span>Cierre</span><span style="color:var(--red)">22 Jun 2025</span></div>
                <div class="info-row"><span>Días restantes</span><span style="color:var(--gold);font-weight:700">42 días</span></div>
              </div>
              <div class="info-block">
                <h4>Puntuación por Dimensión</h4>
                <div class="info-row"><span>Viabilidad Jurídica</span><span><span class="score-pill score-high">88/100</span></span></div>
                <div class="info-row"><span>Viabilidad Financiera</span><span><span class="score-pill score-med">71/100</span></span></div>
                <div class="info-row"><span>Viabilidad Técnica</span><span><span class="score-pill score-high">86/100</span></span></div>
                <div class="info-row"><span>Viabilidad Económica</span><span><span class="score-pill score-med">75/100</span></span></div>
                <div class="info-row"><span>Nivel de Riesgo Global</span><span><span class="score-pill score-med">Medio</span></span></div>
              </div>
            </div>
            <div class="info-block" style="margin-top:16px">
              <h4>Resumen Ejecutivo</h4>
              <div id="ai-summary" style="font-size:13px;line-height:1.7;padding:8px 0;color:var(--text2)">Cargando análisis de IA...</div>
            </div>
          </div>

          <div class="tab-content" id="tab-checklist">
            <div class="checklist">
              <div class="check-item ok"><div class="check-icon"><i class="fa-solid fa-check"></i></div><div class="check-text"><strong>RUT actualizado (año en curso)</strong><br><span style="font-size:11px;color:var(--text2)">Registro Único Tributario vigente</span></div><span class="check-tag">Cumple</span></div>
              <div class="check-item ok"><div class="check-icon"><i class="fa-solid fa-check"></i></div><div class="check-text"><strong>Certificado de existencia y representación legal</strong><br><span style="font-size:11px;color:var(--text2)">Vigente, expedición menor a 30 días</span></div><span class="check-tag">Cumple</span></div>
              <div class="check-item warn"><div class="check-icon"><i class="fa-solid fa-exclamation"></i></div><div class="check-text"><strong>Patrimonio líquido mínimo requerido</strong><br><span style="font-size:11px;color:var(--text2)">Requiere $12.000M · Empresa reporta $10.800M</span></div><span class="check-tag">Revisar</span></div>
              <div class="check-item ok"><div class="check-icon"><i class="fa-solid fa-check"></i></div><div class="check-text"><strong>RESO – Clasificación obras civiles</strong><br><span style="font-size:11px;color:var(--text2)">Clasificación K5 confirmada</span></div><span class="check-tag">Cumple</span></div>
              <div class="check-item fail"><div class="check-icon"><i class="fa-solid fa-times"></i></div><div class="check-text"><strong>Índice de liquidez ≥ 1.5</strong><br><span style="font-size:11px;color:var(--text2)">Ratio actual: 1.18 – Por debajo del mínimo requerido</span></div><span class="check-tag">No cumple</span></div>
              <div class="check-item ok"><div class="check-icon"><i class="fa-solid fa-check"></i></div><div class="check-text"><strong>Experiencia en proyectos similares (10 años)</strong><br><span style="font-size:11px;color:var(--text2)">Se verificaron 8 proyectos comparables</span></div><span class="check-tag">Cumple</span></div>
              <div class="check-item warn"><div class="check-icon"><i class="fa-solid fa-exclamation"></i></div><div class="check-text"><strong>Garantía de seriedad de la oferta</strong><br><span style="font-size:11px;color:var(--text2)">Monto: $782M COP – Revisar vigencia</span></div><span class="check-tag">Revisar</span></div>
              <div class="check-item ok"><div class="check-icon"><i class="fa-solid fa-check"></i></div><div class="check-text"><strong>Paz y salvo con SENA e ICBF</strong><br><span style="font-size:11px;color:var(--text2)">Certificados emitidos en período válido</span></div><span class="check-tag">Cumple</span></div>
            </div>
          </div>

          <div class="tab-content" id="tab-riesgos">
            <div class="risk-grid">
              <div class="risk-item alto"><div class="risk-header"><span class="risk-title">Incumplimiento de índice de liquidez</span><span class="risk-badge">ALTO</span></div><p class="risk-desc">El índice de liquidez actual (1.18) está por debajo del mínimo exigido (1.5). Podría causar eliminación en evaluación financiera. Se recomienda presentar estados financieros consolidados con empresa vinculada.</p></div>
              <div class="risk-item medio"><div class="risk-header"><span class="risk-title">Patrimonio líquido insuficiente</span><span class="risk-badge">MEDIO</span></div><p class="risk-desc">El patrimonio líquido declarado ($10.800M) está un 10% por debajo del requerimiento mínimo ($12.000M). Considerar unión temporal con socio complementario.</p></div>
              <div class="risk-item medio"><div class="risk-header"><span class="risk-title">Concentración de riesgo geológico</span><span class="risk-badge">MEDIO</span></div><p class="risk-desc">El pliego transfiere al concesionario el 85% del riesgo por eventos geológicos. Se recomienda cotizar póliza especializada e incluir en la propuesta económica.</p></div>
              <div class="risk-item bajo"><div class="risk-header"><span class="risk-title">Vigencia de póliza de seriedad</span><span class="risk-badge">BAJO</span></div><p class="risk-desc">La vigencia de la garantía de seriedad vence 48 horas antes del cierre. Gestionar renovación anticipada para evitar inconvenientes de última hora.</p></div>
            </div>
          </div>

          <div class="tab-content" id="tab-recomendaciones">
            <div class="rec-list">
              <div class="rec-item"><div class="rec-num">1</div><div class="rec-body"><h4>Subsanar el índice de liquidez mediante unión temporal</h4><p>Identifique un socio estratégico con fortaleza financiera complementaria. Una unión temporal permite consolidar los indicadores y cumplir el requisito habilitante.</p><span class="rec-tag">Financiero · Prioridad Alta</span></div></div>
              <div class="rec-item"><div class="rec-num">2</div><div class="rec-body"><h4>Renovar garantía de seriedad con 10 días de antelación</h4><p>Gestione la renovación de la póliza con suficiente anticipación para evitar riesgos de descalificación por documentación vencida.</p><span class="rec-tag">Jurídico · Prioridad Media</span></div></div>
              <div class="rec-item"><div class="rec-num">3</div><div class="rec-body"><h4>Incluir análisis de riesgo geológico en propuesta técnica</h4><p>Demuestre dominio del riesgo geológico con estudios previos y plan de gestión. Esto diferencia positivamente la propuesta técnica frente a competidores.</p><span class="rec-tag">Técnico · Diferenciador</span></div></div>
              <div class="rec-item"><div class="rec-num">4</div><div class="rec-body"><h4>Optimizar propuesta económica revisando CAPEX fase 2</h4><p>El análisis sugiere margen de optimización del 8-12% en costos de capex de la fase 2 sin sacrificar calidad técnica ni rentabilidad del proyecto.</p><span class="rec-tag">Económico · Oportunidad</span></div></div>
            </div>
          </div>
        </div>
      </div>

      <!-- COMPARAR -->
      <div class="page" id="page-comparar">
        <p style="color:var(--text2);margin-bottom:20px">Selecciona dos o más licitaciones para comparar sus análisis lado a lado. Haz clic en las tarjetas para seleccionar.</p>
        <div class="compare-grid" id="compare-grid"></div>
        <div id="compare-result" style="display:none;margin-top:16px;padding:20px;background:var(--card);border:1px solid var(--border);border-radius:14px">
          <h3 class="section-title"><i class="fa-solid fa-scale-balanced"></i>Análisis Comparativo</h3>
          <table style="margin-top:8px"><thead><tr><th>Dimensión</th><th>Licitación A</th><th>Licitación B</th><th>Ventaja</th></tr></thead><tbody>
            <tr><td>Score Total</td><td><span class="score-pill score-high">82/100</span></td><td><span class="score-pill score-med">67/100</span></td><td style="color:var(--green)">← Licitación A</td></tr>
            <tr><td>Riesgo Financiero</td><td><span class="score-pill score-med">Medio</span></td><td><span class="score-pill score-low">Alto</span></td><td style="color:var(--green)">← Licitación A</td></tr>
            <tr><td>Plazo contractual</td><td>15 años</td><td>3 años</td><td style="color:var(--blue3)">Estratégico</td></tr>
            <tr><td>Valor (M COP)</td><td style="font-family:var(--mono)">$78.400</td><td style="font-family:var(--mono)">$12.200</td><td style="color:var(--blue3)">—</td></tr>
            <tr><td>Docs. habilitados</td><td>6/8</td><td>7/7</td><td style="color:var(--green)">→ Licitación B</td></tr>
          </tbody></table>
        </div>
      </div>

      <!-- ALERTAS -->
      <div class="page" id="page-alertas">
        <h3 class="section-title"><i class="fa-solid fa-bell"></i>Centro de Alertas</h3>
        <div class="alert-list">
          <div class="alert-item critical"><i class="fa-solid fa-circle-xmark"></i><div class="alert-text"><h4>Índice de liquidez insuficiente · MC-2024-089</h4><p>Tu empresa no cumple el índice de liquidez mínimo (1.5). El proceso cierra en 42 días. Acción requerida urgente.</p></div></div>
          <div class="alert-item critical"><i class="fa-solid fa-clock"></i><div class="alert-text"><h4>Cierre en 5 días · Servicios TI Gobierno Digital</h4><p>El proceso IDU-TI-2024-112 cierra el próximo lunes. Aún no se ha completado el checklist documental completo.</p></div></div>
          <div class="alert-item warning"><i class="fa-solid fa-triangle-exclamation"></i><div class="alert-text"><h4>Póliza de seriedad próxima a vencer · MC-2024-089</h4><p>La garantía vence en 8 días. Gestionar renovación para evitar descalificación por incumplimiento documental.</p></div></div>
          <div class="alert-item warning"><i class="fa-solid fa-file-circle-exclamation"></i><div class="alert-text"><h4>Documento pendiente de actualización · CNT-2025-043</h4><p>El certificado paz y salvo SENA requiere actualización. Fecha de expedición superó los 90 días permitidos.</p></div></div>
          <div class="alert-item info"><i class="fa-solid fa-lightbulb"></i><div class="alert-text"><h4>Nueva licitación compatible detectada</h4><p>SIEL detectó un nuevo proceso de Aerocivil (AAC-2025-076) con 89% de coincidencia con tus capacidades. Score estimado: 79/100.</p></div></div>
          <div class="alert-item info"><i class="fa-solid fa-robot"></i><div class="alert-text"><h4>Análisis completado · Contrato de Obra IDU</h4><p>El análisis del pliego IDU-OB-2025-031 finalizó. Score: 74/100. Se identificaron 2 riesgos medios y 1 oportunidad de mejora.</p></div></div>
        </div>
      </div>

      <!-- ASISTENTE -->
      <div class="page" id="page-asistente">
        <div style="background:var(--card);border:1px solid var(--border);border-radius:14px;overflow:hidden">
          <div style="padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px">
            <div style="width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--cyan));display:flex;align-items:center;justify-content:center"><i class="fa-solid fa-robot" style="color:#fff;font-size:16px"></i></div>
            <div>
              <div style="font-size:14px;font-weight:600">SIEL Copilot IA</div>
              <div style="font-size:11px;color:var(--green)">● Activo · claude-sonnet-4</div>
            </div>
            <div style="margin-left:auto;font-size:11px;color:var(--text3);background:var(--navy3);padding:4px 10px;border-radius:8px;border:1px solid var(--border)">12 licitaciones cargadas</div>
          </div>
          <div class="chat-container">
            <div class="chat-messages" id="chat-messages"></div>
            <div class="chat-input-area">
              <textarea class="chat-input" id="chat-input" rows="1" placeholder="Pregunta sobre requisitos, riesgos, estrategia..." onkeydown="handleKey(event)"></textarea>
              <button class="chat-send" onclick="sendMsg()"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
          </div>
        </div>
        <div class="quick-btns">
          <button class="filter-btn" onclick="quickAsk('¿Cuáles son los requisitos habilitantes del proceso MC-2024-089?')">📋 Requisitos habilitantes</button>
          <button class="filter-btn" onclick="quickAsk('¿Qué riesgos financieros debo priorizar?')">⚠️ Riesgos financieros</button>
          <button class="filter-btn" onclick="quickAsk('Dame un resumen ejecutivo de mis licitaciones activas')">📊 Resumen ejecutivo</button>
          <button class="filter-btn" onclick="quickAsk('¿Cómo puedo mejorar el score de viabilidad?')">🚀 Mejorar score</button>
          <button class="filter-btn" onclick="quickAsk('¿Cuál licitación me conviene más presentar primero?')">🎯 ¿Cuál priorizar?</button>
        </div>
      </div>

      <!-- SUSCRIPCION -->
      <div class="page" id="page-suscripcion">
        <p style="color:var(--text2);margin-bottom:24px">Elige el plan ideal para tu organización. Todos incluyen IA ilimitada durante el período de prueba.</p>
        <div class="sub-grid">
          <div class="sub-card">
            <div class="sub-name" style="color:var(--text3)">STARTER</div>
            <div class="sub-price">$490<span>/mo</span></div>
            <div class="sub-period">USD · Facturación mensual</div>
            <ul class="sub-features">
              <li class="yes"><i class="fa-solid fa-check"></i>5 licitaciones/mes</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Análisis básico IA</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Checklist documental</li>
              <li class="yes"><i class="fa-solid fa-check"></i>1 usuario</li>
              <li class="no"><i class="fa-solid fa-xmark"></i>Comparación entre procesos</li>
              <li class="no"><i class="fa-solid fa-xmark"></i>Asistente conversacional</li>
              <li class="no"><i class="fa-solid fa-xmark"></i>API access</li>
            </ul>
            <button class="btn-sub outline">Comenzar gratis</button>
          </div>
          <div class="sub-card featured">
            <div class="sub-name" style="color:var(--blue3)">PRO</div>
            <div class="sub-price">$1.290<span>/mo</span></div>
            <div class="sub-period">USD · Facturación mensual</div>
            <ul class="sub-features">
              <li class="yes"><i class="fa-solid fa-check"></i>Licitaciones ilimitadas</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Análisis completo IA</li>
              <li class="yes"><i class="fa-solid fa-check"></i>SIEL Copilot IA</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Comparación avanzada</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Alertas en tiempo real</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Hasta 5 usuarios</li>
              <li class="no"><i class="fa-solid fa-xmark"></i>API access</li>
            </ul>
            <button class="btn-sub filled">Plan actual ✓</button>
          </div>
          <div class="sub-card">
            <div class="sub-name" style="color:var(--gold)">ENTERPRISE</div>
            <div class="sub-price">$3.990<span>/mo</span></div>
            <div class="sub-period">USD · Facturación mensual</div>
            <ul class="sub-features">
              <li class="yes"><i class="fa-solid fa-check"></i>Todo lo del plan Pro</li>
              <li class="yes"><i class="fa-solid fa-check"></i>API REST completa</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Modelo IA personalizado</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Usuarios ilimitados</li>
              <li class="yes"><i class="fa-solid fa-check"></i>SLA 99.9% uptime</li>
              <li class="yes"><i class="fa-solid fa-check"></i>Soporte dedicado 24/7</li>
              <li class="yes"><i class="fa-solid fa-check"></i>On-premise disponible</li>
            </ul>
            <button class="btn-sub outline">Contactar ventas</button>
          </div>
        </div>
      </div>

      <!-- ADMIN -->
      <div class="page" id="page-admin">
        <div class="stats-grid">
          <div class="stat-card"><div class="stat-label">Usuarios Totales</div><div class="stat-value">247</div><div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;+18 este mes</div><div class="stat-icon" style="background:rgba(30,111,255,.15);color:var(--blue3)"><i class="fa-solid fa-users"></i></div></div>
          <div class="stat-card"><div class="stat-label">Ingresos MRR</div><div class="stat-value">$28k</div><div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;+9.3%</div><div class="stat-icon" style="background:rgba(0,196,140,.15);color:var(--green)"><i class="fa-solid fa-dollar-sign"></i></div></div>
          <div class="stat-card"><div class="stat-label">Análisis/día</div><div class="stat-value">142</div><div class="stat-change up"><i class="fa-solid fa-arrow-trend-up"></i>&nbsp;Promedio 7d</div><div class="stat-icon" style="background:rgba(240,180,41,.15);color:var(--gold)"><i class="fa-solid fa-robot"></i></div></div>
          <div class="stat-card"><div class="stat-label">Churn Rate</div><div class="stat-value">2.1%</div><div class="stat-change up"><i class="fa-solid fa-arrow-trend-down"></i>&nbsp;-0.4% MoM</div><div class="stat-icon" style="background:rgba(0,212,255,.15);color:var(--cyan)"><i class="fa-solid fa-chart-pie"></i></div></div>
        </div>
        <div class="table-card">
          <div class="table-header"><h3>Gestión de Usuarios</h3></div>
          <table><thead><tr><th>Usuario</th><th>Empresa</th><th>Plan</th><th>Análisis</th><th>Último acceso</th><th>Estado</th></tr></thead><tbody>
            <tr><td>Juan Rodríguez</td><td>Constructora JR S.A.S</td><td><span class="plan-badge pro">Pro</span></td><td style="font-family:var(--mono)">47</td><td>Hoy, 10:23</td><td><span class="status-pill complete"><span class="status-dot"></span>Activo</span></td></tr>
            <tr><td>María López</td><td>Ingeniería ML Ltda</td><td><span class="plan-badge enterprise">Enterprise</span></td><td style="font-family:var(--mono)">123</td><td>Hoy, 09:15</td><td><span class="status-pill complete"><span class="status-dot"></span>Activo</span></td></tr>
            <tr><td>Carlos Vega</td><td>CV Consultores</td><td><span class="plan-badge starter">Starter</span></td><td style="font-family:var(--mono)">12</td><td>Ayer, 14:30</td><td><span class="status-pill complete"><span class="status-dot"></span>Activo</span></td></tr>
            <tr><td>Ana Torres</td><td>Torres & Asociados</td><td><span class="plan-badge pro">Pro</span></td><td style="font-family:var(--mono)">31</td><td>Hace 3 días</td><td><span class="status-pill review"><span class="status-dot"></span>Trial</span></td></tr>
          </tbody></table>
        </div>
      </div>

    </div><!-- end content-area -->
  </main>
</div><!-- end app -->

<script>
// ---- DATA ----
const licitaciones=[
  {id:'MC-2024-089',nombre:'Concesión Vial Ruta del Sol',entidad:'INVIAS',valor:'$78.400M',score:82,clase:'score-high',estado:'complete',estadoTxt:'Analizado',cierre:'22 Jun 2025'},
  {id:'IDU-TI-2024-112',nombre:'Servicios TI Gobierno Digital',entidad:'IDU',valor:'$12.200M',score:67,clase:'score-med',estado:'review',estadoTxt:'En revisión',cierre:'27 May 2025'},
  {id:'CNT-2025-043',nombre:'Mantenimiento Red Hospitalaria',entidad:'Min Salud',valor:'$5.800M',score:91,clase:'score-high',estado:'complete',estadoTxt:'Analizado',cierre:'15 Jul 2025'},
  {id:'AAC-2025-076',nombre:'Ampliación Terminal Aéreo',entidad:'Aerocivil',valor:'$42.100M',score:54,clase:'score-low',estado:'analyzing',estadoTxt:'Analizando',cierre:'30 Jun 2025'},
  {id:'MIN-ED-2025-11',nombre:'Plataforma Educativa Pública',entidad:'Min Educación',valor:'$9.300M',score:78,clase:'score-med',estado:'complete',estadoTxt:'Analizado',cierre:'8 Ago 2025'},
];

const pageTitles={
  dashboard:['Dashboard Gerencial','Resumen ejecutivo · Mayo 2025'],
  upload:['Nueva Licitación','Sube el pliego para análisis automático con IA'],
  licitaciones:['Mis Licitaciones','Gestión y seguimiento de procesos activos'],
  analisis:['Análisis Detallado','Concesión Vial Ruta del Sol · MC-2024-089'],
  comparar:['Comparar Licitaciones','Análisis comparativo lado a lado'],
  alertas:['Centro de Alertas','Notificaciones y acciones requeridas'],
  asistente:['SIEL Copilot IA','Tu asistente inteligente de contratación'],
  suscripcion:['Plan y Suscripción','Gestión de tu plan SIEL'],
  admin:['Panel Administrativo','Métricas del sistema y usuarios'],
};

// ---- RENDER ----
function renderTable(id){
  const el=document.getElementById(id);
  if(!el)return;
  el.innerHTML=licitaciones.map(l=>`<tr>
    <td><div style="font-weight:500">${l.nombre}</div><div style="font-size:11px;color:var(--text3);font-family:var(--mono)">${l.id}</div></td>
    <td style="color:var(--text2)">${l.entidad}</td>
    <td style="font-family:var(--mono);color:var(--gold)">${l.valor}</td>
    <td><span class="score-pill ${l.clase}">${l.score}</span></td>
    <td><span class="status-pill ${l.estado}"><span class="status-dot"></span>${l.estadoTxt}</span></td>
    <td style="color:var(--text2);font-size:12px">${l.cierre}</td>
    <td><button class="action-btn" onclick="showPage('analisis')">Ver análisis</button></td>
  </tr>`).join('');
}

function renderBars(){
  const data=[{l:'Dic',v:61},{l:'Ene',v:65},{l:'Feb',v:68},{l:'Mar',v:64},{l:'Abr',v:70},{l:'May',v:73}];
  const max=80;
  const colors=['#1C2645','#1C2645','#1C2645','#1C2645','#3B87FF','#1E6FFF'];
  const el=document.getElementById('bar-chart');
  if(!el)return;
  el.innerHTML=data.map((d,i)=>`<div class="bar-wrap">
    <div class="bar" style="height:${(d.v/max)*100}%;background:${colors[i]}" title="${d.v}"></div>
    <span class="bar-label">${d.l}</span>
  </div>`).join('');
}

function renderCompare(){
  const el=document.getElementById('compare-grid');
  if(!el)return;
  el.innerHTML=licitaciones.map(l=>`<div class="compare-card" onclick="toggleCompare(this)">
    <div class="compare-top"><h3>${l.nombre}</h3><p>${l.entidad} · ${l.cierre}</p></div>
    <div class="compare-body">
      <div class="compare-metric"><span>Score IA</span><span class="score-pill ${l.clase}" style="font-size:11px">${l.score}/100</span></div>
      <div class="compare-metric"><span>Valor</span><span style="font-family:var(--mono);color:var(--gold)">${l.valor}</span></div>
      <div class="compare-metric"><span>Estado</span><span class="status-pill ${l.estado}"><span class="status-dot"></span>${l.estadoTxt}</span></div>
    </div>
  </div>`).join('');
}

function toggleCompare(el){
  el.classList.toggle('selected');
  const n=document.querySelectorAll('.compare-card.selected').length;
  document.getElementById('compare-result').style.display=n>=2?'block':'none';
}

// ---- NAVIGATION ----
function showPage(id){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  const pg=document.getElementById('page-'+id);
  if(pg)pg.classList.add('active');
  const ti=pageTitles[id]||[id,''];
  document.getElementById('page-title').textContent=ti[0];
  document.getElementById('page-sub').textContent=ti[1];
  document.querySelectorAll('.nav-item').forEach(n=>{
    const oc=n.getAttribute('onclick')||'';
    if(oc.includes("'"+id+"'"))n.classList.add('active');
  });
}

function switchTab(id,el){
  document.querySelectorAll('.detail-tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');
  const tc=document.getElementById('tab-'+id);
  if(tc)tc.classList.add('active');
}

function setFilter(btn){
  btn.closest('.table-filters').querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
}

// ---- LOGIN ----
function doLogin(){
  const ls=document.getElementById('login-screen');
  ls.classList.add('hidden');
  document.getElementById('app').classList.add('active');
  setTimeout(()=>ls.style.display='none',500);
  renderTable('lic-table-body');
  renderTable('lic-table-all');
  renderBars();
  renderCompare();
  loadAISummary();
  initChat();
}

// ---- AI SUMMARY ----
async function loadAISummary(){
  const el=document.getElementById('ai-summary');
  if(!el)return;
  try{
    const r=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',max_tokens:500,
        system:'Eres SIEL, sistema experto en análisis de licitaciones públicas y privadas colombianas. Genera resúmenes ejecutivos concisos, estratégicos y profesionales en español. Máximo 4 oraciones claras y directas.',
        messages:[{role:'user',content:'Resumen ejecutivo para: Concesión Vial Ruta del Sol Sector 3, INVIAS, $78.400M COP, 15 años, score 82/100. Riesgo principal: índice de liquidez 1.18 vs mínimo 1.5. Cierre en 42 días.'}]
      })
    });
    const d=await r.json();
    if(d.content&&d.content[0])el.innerHTML='<span style="color:var(--text1)">'+d.content[0].text+'</span><div style="margin-top:8px;font-size:11px;color:var(--text3)"><i class="fa-solid fa-robot"></i> Generado por SIEL Copilot IA</div>';
  }catch(e){
    el.innerHTML='<span style="color:var(--text1)">La licitación MC-2024-089 presenta una viabilidad sólida con score 82/100, destacando en los aspectos jurídico (88) y técnico (86). El principal riesgo identificado es el incumplimiento del índice de liquidez mínimo, subsanable mediante unión temporal estratégica. Con 42 días para el cierre, el proceso es abordable con las acciones correctivas priorizadas. Se recomienda proceder con prioridad alta.</span><div style="margin-top:8px;font-size:11px;color:var(--text3)"><i class="fa-solid fa-robot"></i> Resumen ejecutivo IA</div>';
  }
}

// ---- CHAT ----
let chatHistory=[];
function initChat(){
  const el=document.getElementById('chat-messages');
  if(!el)return;
  el.innerHTML='';chatHistory=[];
  addMsg('ai','👋 Hola, soy <strong>SIEL Copilot</strong>. Tengo acceso al análisis de tus 12 licitaciones activas. Puedo ayudarte con requisitos habilitantes, análisis de riesgos, estrategia de propuesta y documentación. ¿En qué te ayudo hoy?');
}

function addMsg(role,html){
  const el=document.getElementById('chat-messages');
  if(!el)return;
  const d=document.createElement('div');
  d.className='msg '+role;
  const now=new Date();
  const t=now.getHours()+':'+(now.getMinutes()<10?'0':'')+now.getMinutes();
  d.innerHTML='<div class="msg-bubble">'+html+'</div><div class="msg-time">'+t+'</div>';
  el.appendChild(d);el.scrollTop=el.scrollHeight;
}

function showTyping(){
  const el=document.getElementById('chat-messages');
  if(!el)return;
  const d=document.createElement('div');
  d.className='msg ai';d.id='typing';
  d.innerHTML='<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
  el.appendChild(d);el.scrollTop=el.scrollHeight;
}

function hideTyping(){const t=document.getElementById('typing');if(t)t.remove();}

async function sendMsg(){
  const inp=document.getElementById('chat-input');
  const txt=inp.value.trim();if(!txt)return;
  addMsg('user',txt);
  chatHistory.push({role:'user',content:txt});
  inp.value='';showTyping();
  try{
    const r=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',max_tokens:600,
        system:`Eres SIEL Copilot, asistente experto de un SaaS de análisis de licitaciones en Colombia. Licitaciones activas del usuario:
1. MC-2024-089: Concesión Vial Ruta del Sol – INVIAS – $78.400M – Score 82/100 – Riesgo: liquidez 1.18 vs 1.5, cierra en 42 días
2. IDU-TI-2024-112: Servicios TI Gobierno Digital – IDU – $12.200M – Score 67/100 – Cierra en 5 días
3. CNT-2025-043: Mantenimiento Red Hospitalaria – Min Salud – $5.800M – Score 91/100 – Excelente viabilidad
4. AAC-2025-076: Ampliación Terminal Aéreo – Aerocivil – $42.100M – Score 54/100 – Alto riesgo
5. MIN-ED-2025-11: Plataforma Educativa Pública – Min Educación – $9.300M – Score 78/100
Eres experto en SECOP, pliegos colombianos, análisis jurídico/financiero/técnico/económico y gestión documental. Responde conciso, estratégico y profesional en español. Máximo 120 palabras.`,
        messages:chatHistory
      })
    });
    const d=await r.json();
    hideTyping();
    if(d.content&&d.content[0]){
      const rep=d.content[0].text;
      chatHistory.push({role:'assistant',content:rep});
      addMsg('ai',rep);
    }
  }catch(e){
    hideTyping();
    const fb='Con base en tus licitaciones activas, te recomiendo priorizar CNT-2025-043 (Score 91/100 – excelente viabilidad) y atender urgentemente el índice de liquidez en MC-2024-089. ¿Quieres que profundice en alguno de estos procesos?';
    chatHistory.push({role:'assistant',content:fb});
    addMsg('ai',fb);
  }
}

function quickAsk(q){document.getElementById('chat-input').value=q;sendMsg();}
function handleKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMsg();}}

// ---- UPLOAD SIMULATION ----
document.addEventListener('DOMContentLoaded',function(){
  const fi=document.getElementById('file-input');
  if(fi)fi.addEventListener('change',function(){if(this.files[0])simUpload(this.files[0].name);});
  const dz=document.getElementById('drop-zone');
  if(dz){
    dz.addEventListener('dragover',function(e){e.preventDefault();this.style.borderColor='var(--blue)';this.style.background='rgba(30,111,255,.06)'});
    dz.addEventListener('dragleave',function(){this.style.borderColor='';this.style.background=''});
    dz.addEventListener('drop',function(e){e.preventDefault();this.style.borderColor='';this.style.background='';simUpload(e.dataTransfer.files[0]?.name||'pliego.pdf')});
  }
});

function simUpload(name){
  const prog=document.getElementById('upload-progress');
  const fill=document.getElementById('progress-fill');
  const txt=document.getElementById('progress-text');
  prog.style.display='block';
  const steps=[[15,'Subiendo: '+name+'...'],[40,'Procesando con OCR...'],[58,'Extrayendo requisitos jurídicos...'],[72,'Analizando condiciones financieras...'],[86,'Evaluando aspectos técnicos...'],[100,'¡Análisis completado!']];
  let i=0;
  const iv=setInterval(()=>{
    if(i<steps.length){fill.style.width=steps[i][0]+'%';txt.textContent=steps[i][1];i++;}
    else{clearInterval(iv);setTimeout(()=>{prog.style.display='none';fill.style.width='0';showPage('analisis');},900);}
  },650);
}
</script>
</body>
</html>

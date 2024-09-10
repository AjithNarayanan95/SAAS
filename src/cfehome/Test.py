import re
import json
import os

# HTML content (replace this with the actual HTML content or file reading logic)
html_content = '''


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>RcopiaTest Report</title>
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@b00a2d0486596e73dd7326beacf352c639623a0e/commons/img/logo.png">
<link rel="shortcut icon" href="https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@b00a2d0486596e73dd7326beacf352c639623a0e/commons/img/logo.png">
<link href="https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@d6562a79075e061305ccfdb82f01e5e195e2d307/spark/css/spark-style.css" rel="stylesheet" />
<link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@7cc78ce/spark/js/jsontree.js"></script>
<style type="text/css"></style></head><body class="spa -report standard">
  <div class="app">
    <div class="layout">
<div class="header navbar">
<div class="vheader">
<div class="nav-logo">
<a href="#">
<div class="logo" style="background-image: url('https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@b00a2d0486596e73dd7326beacf352c639623a0e/commons/img/logo.png')"></div>
</a>
</div>
<ul class="nav-left">
<li class="search-box">
<a class="search-toggle" href="#">
<i class="search-icon fa fa-search"></i>
<i class="search-icon-close fa fa-close"></i>
</a>
</li>
<li class="search-input"><input id="search-tests" class="form-control" type="text" placeholder="Search..."></li>
</ul>
<ul class="nav-right">
<li class="m-r-10">
<a href="#"><span class="badge badge-primary">Eagle SP2</span></a>
</li>
<li class="m-r-10">
<a href="#"><span class="badge badge-primary">Sep 9, 2024 11:56:57 AM</span></a>
</li>
</ul>
</div>
</div><div class="side-nav">
<div class="side-nav-inner">
<ul class="side-nav-menu">
<li class="nav-item dropdown" onclick="toggleView('test-view')">
<a id="nav-test" class="dropdown-toggle" href="#">
<span class="ico"><i class="fa fa-list"></i></span>
</a>
</li>
<li class="nav-item dropdown" onclick="toggleView('dashboard-view')">
<a id="nav-dashboard" class="dropdown-toggle" href="#">
<span class="ico"><i class="fa fa-bar-chart"></i></span>
</a>
</li>
</ul>
</div>
</div>      <div class="vcontainer">
        <div class="main-content">
<div class="test-wrapper row view test-view">
  <div class="test-list">
    <div class="test-list-tools">
<ul class="tools pull-left">
<li><a href="#"><span class="font-size-14">Tests</span></a></li>
</ul>
<ul class="tools text-right">
<li class="dropdown">
<a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-exclamation-circle"></i></a>
<ul id="status-toggle" class="dropdown-menu dropdown-md p-v-0">
<a class="dropdown-item" status="pass" href="#"><span>Pass</span><span class="status success"></span></a>
<div class="dropdown-divider"></div>
<a status="clear" class="dropdown-item" href="#"><span>Clear</span><span class="pull-right"><i class="fa fa-close"></i></span></a>
</ul>
</li>
</ul>
</div>    <div class="test-list-wrapper scrollable">
      <ul class="test-list-item">
        <li class="test-item"  status="pass" test-id="1"
          author=""
          tag=""
          device="">
          <div class="test-detail">
            <p class="name">UserRegistration</p>
            <p class="text-sm">
              <span>11:56:57 AM</span> / <span>00:19:14:538</span>
              <span class="badge pass-bg log float-right">Pass</span>
            </p>
          </div>
          <div class="test-contents d-none">
<div class="detail-head">
<div class="p-v-10">
<div class="info">
<h5 class="test-status text-pass">UserRegistration</h5>
<span class='badge badge-success'>09.09.2024 11:56:57 AM</span>
<span class='badge badge-danger'>09.09.2024 12:16:12 PM</span>
<span class='badge badge-default'>00:19:14:538</span>
&middot; <span class='uri-anchor badge badge-default'>#test-id=1</span>
<span class='badge badge-default pointer float-right ml-1 et'><i class="fa fa-chevron-down"></i></span>
<span class='badge badge-default pointer float-right ct'><i class="fa fa-chevron-up"></i></span>
</div>
</div>
</div><div class="detail-body mt-4">
<table class="table table-sm">
  <thead><tr><th class="status-col">Status</th><th class="timestamp-col">Timestamp</th><th class="details-col">Details</th></tr></thead>
  <tbody>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:56:58 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:08 AM</td>
        <td>
          Generated practiceUsername is: ve37894 and vendorUsername: nnewvendor3527 and vendorPassword: hm4zdoc1
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:09 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830949 and practiceId: 22320066462 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:09 AM</td>
        <td>
          LocationId: 22113852485
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:10 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:10 AM</td>
        <td>
          Username: flqrfread1250, Password: 76tgeebv (encrypted: kN7TtTmSdVSjd4ME4hrVDw==), SystemName: auto_qa_mhsqmlpdpx, UserFirstName: Fajwauke, UserLastName: Lqrfread, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:13 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:15 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fajwauke","userLastName":"Lqrfread","username":"flqrfread1250","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_mhsqmlpdpx","practiceUsername":"ve37894","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:15 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:15 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:21 AM</td>
        <td>
          Generated practiceUsername is: hw37891 and vendorUsername: nnewvendor7391 and vendorPassword: eiz9qz3y
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:21 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830950 and practiceId: 22320066492 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:21 AM</td>
        <td>
          LocationId: 22113852486
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:22 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:23 AM</td>
        <td>
          Username: flyzsjiux1574, Password: 5khkeq9m (encrypted: geGcqb6m6DYpy6bZEmZfXQ==), SystemName: auto_qa_dczkvvsmrv, UserFirstName: Fmxxvnng, UserLastName: Lyzsjiux, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:24 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:26 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmxxvnng","userLastName":"Lyzsjiux","username":"flyzsjiux1574","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_dczkvvsmrv","practiceUsername":"hw37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:26 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:26 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:31 AM</td>
        <td>
          Generated practiceUsername is: lv3789 and vendorUsername: nnewvendor1067 and vendorPassword: n4wjalst
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:32 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830951 and practiceId: 22320066522 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:32 AM</td>
        <td>
          LocationId: 22113852487
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:33 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:33 AM</td>
        <td>
          Username: flvoadjzp1211, Password: h46zalss (encrypted: e2WeCbtJMrtnvQ5d4mIfPA==), SystemName: auto_qa_rbhpewqauk, UserFirstName: Fdlqgavg, UserLastName: Lvoadjzp, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:34 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:36 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fdlqgavg","userLastName":"Lvoadjzp","username":"flvoadjzp1211","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rbhpewqauk","practiceUsername":"lv3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:36 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:36 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:41 AM</td>
        <td>
          Generated practiceUsername is: lc3789 and vendorUsername: nnewvendor6110 and vendorPassword: 6mk65014
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:42 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830952 and practiceId: 22320066552 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:42 AM</td>
        <td>
          LocationId: 22113852488
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:43 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:43 AM</td>
        <td>
          Username: flxykwgre1001, Password: ih8nvx3v (encrypted: pgDkOC3yIPvXoo45FQQcbw==), SystemName: auto_qa_qlultxbsqn, UserFirstName: Fhjvynuv, UserLastName: Lxykwgre, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:44 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:46 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhjvynuv","userLastName":"Lxykwgre","username":"flxykwgre1001","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qlultxbsqn","practiceUsername":"lc3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:46 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:46 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:50 AM</td>
        <td>
          Generated practiceUsername is: pv3789 and vendorUsername: nnewvendor2636 and vendorPassword: qfheo4ij
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:51 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830953 and practiceId: 22320066582 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:51 AM</td>
        <td>
          LocationId: 22113852489
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:52 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:53 AM</td>
        <td>
          Username: fllerhslp1551, Password: z8vjou4m (encrypted: Zawas8FkPSK42etD4p/+Ew==), SystemName: auto_qa_sbxyddzwex, UserFirstName: Feoncytp, UserLastName: Llerhslp, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:53 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:55 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Feoncytp","userLastName":"Llerhslp","username":"fllerhslp1551","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_sbxyddzwex","practiceUsername":"pv3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:55 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:57:55 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:00 AM</td>
        <td>
          Generated practiceUsername is: jr37891 and vendorUsername: nnewvendor8417 and vendorPassword: wlddyum2
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:00 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830954 and practiceId: 22320066612 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:00 AM</td>
        <td>
          LocationId: 22113852490
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:02 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:02 AM</td>
        <td>
          Username: flgktnibk1755, Password: 2lew0tcy (encrypted: dnC616MuEc+3mU2qDBJNrg==), SystemName: auto_qa_kclyvpyahn, UserFirstName: Fnsncgvk, UserLastName: Lgktnibk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:02 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:05 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fnsncgvk","userLastName":"Lgktnibk","username":"flgktnibk1755","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_kclyvpyahn","practiceUsername":"jr37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:05 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:05 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:12 AM</td>
        <td>
          Generated practiceUsername is: ep378910 and vendorUsername: nnewvendor9015 and vendorPassword: h2k4j6el
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:12 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830955 and practiceId: 22320066642 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:12 AM</td>
        <td>
          LocationId: 22113852491
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:14 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:14 AM</td>
        <td>
          Username: flqjedsud1568, Password: bp43pz45 (encrypted: tSplTP2p2iqCttQrcJf8fg==), SystemName: auto_qa_bbfnmvcmld, UserFirstName: Fsfwstmy, UserLastName: Lqjedsud, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:15 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:17 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fsfwstmy","userLastName":"Lqjedsud","username":"flqjedsud1568","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_bbfnmvcmld","practiceUsername":"ep378910","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:17 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:17 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:22 AM</td>
        <td>
          Generated practiceUsername is: ai37891 and vendorUsername: nnewvendor7095 and vendorPassword: aagd2klp
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:23 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830956 and practiceId: 22320066672 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:23 AM</td>
        <td>
          LocationId: 22113852492
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:24 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:24 AM</td>
        <td>
          Username: flwhnnolv1472, Password: 1dzejkqa (encrypted: iTDjnMoF+ZRMXWzn+ClLdA==), SystemName: auto_qa_pfhvviqffv, UserFirstName: Fftbhvmn, UserLastName: Lwhnnolv, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:25 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:27 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fftbhvmn","userLastName":"Lwhnnolv","username":"flwhnnolv1472","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_pfhvviqffv","practiceUsername":"ai37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:27 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:27 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:33 AM</td>
        <td>
          Generated practiceUsername is: gw37891 and vendorUsername: nnewvendor5170 and vendorPassword: 54nyj6ny
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:34 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830957 and practiceId: 22320066702 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:34 AM</td>
        <td>
          LocationId: 22113852493
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:35 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:35 AM</td>
        <td>
          Username: flvwrwyfz1331, Password: 828ikaw6 (encrypted: z0kI0ZmxqTDCrFbcedJWbA==), SystemName: auto_qa_bfppddqnpd, UserFirstName: Fbvklpeu, UserLastName: Lvwrwyfz, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:36 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:39 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fbvklpeu","userLastName":"Lvwrwyfz","username":"flvwrwyfz1331","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_bfppddqnpd","practiceUsername":"gw37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:39 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:39 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:46 AM</td>
        <td>
          Generated practiceUsername is: yb37891 and vendorUsername: nnewvendor1251 and vendorPassword: 5h11hmny
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:46 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830958 and practiceId: 22320066732 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:46 AM</td>
        <td>
          LocationId: 22113852494
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:48 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:48 AM</td>
        <td>
          Username: flevnvwwk1720, Password: jc6i1gkn (encrypted: /BsETN42havtPnKeIMJVgw==), SystemName: auto_qa_wuqqxgsqfn, UserFirstName: Fsegtfhe, UserLastName: Levnvwwk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:49 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:51 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fsegtfhe","userLastName":"Levnvwwk","username":"flevnvwwk1720","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_wuqqxgsqfn","practiceUsername":"yb37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:51 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:51 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:57 AM</td>
        <td>
          Generated practiceUsername is: mj37891 and vendorUsername: nnewvendor5473 and vendorPassword: phk1pp7c
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:58 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830959 and practiceId: 22320066762 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:58 AM</td>
        <td>
          LocationId: 22113852495
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:59 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:59 AM</td>
        <td>
          Username: fldityvva1836, Password: sowzi9jy (encrypted: M02DHJoXFcsSrYcgPV0ERg==), SystemName: auto_qa_jgqueqwdte, UserFirstName: Fmdvwlez, UserLastName: Ldityvva, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:58:59 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:02 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmdvwlez","userLastName":"Ldityvva","username":"fldityvva1836","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jgqueqwdte","practiceUsername":"mj37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:02 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:02 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:09 AM</td>
        <td>
          Generated practiceUsername is: gs37891 and vendorUsername: nnewvendor4884 and vendorPassword: oguu99r5
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:09 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830960 and practiceId: 22320066792 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:09 AM</td>
        <td>
          LocationId: 22113852496
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:11 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:11 AM</td>
        <td>
          Username: flskafxrs1759, Password: uz6cdx8i (encrypted: B8FpTdThPtCRtrEdWXxhsA==), SystemName: auto_qa_tcnjakdhkn, UserFirstName: Fkzxqpbo, UserLastName: Lskafxrs, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:12 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:14 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fkzxqpbo","userLastName":"Lskafxrs","username":"flskafxrs1759","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_tcnjakdhkn","practiceUsername":"gs37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:14 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:14 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:21 AM</td>
        <td>
          Generated practiceUsername is: jo37891 and vendorUsername: nnewvendor6336 and vendorPassword: w2n8i4kc
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:22 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830961 and practiceId: 22320066822 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:22 AM</td>
        <td>
          LocationId: 22113852497
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:23 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:24 AM</td>
        <td>
          Username: flpjxrotv1863, Password: 8vlleea9 (encrypted: LemijsfIdp4Icv+cbMeVAQ==), SystemName: auto_qa_wltlljmvfb, UserFirstName: Fhblspgb, UserLastName: Lpjxrotv, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:24 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:27 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhblspgb","userLastName":"Lpjxrotv","username":"flpjxrotv1863","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_wltlljmvfb","practiceUsername":"jo37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:27 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:27 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:35 AM</td>
        <td>
          Generated practiceUsername is: op37891 and vendorUsername: nnewvendor4834 and vendorPassword: tas5l2u9
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:35 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830962 and practiceId: 22320066852 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:35 AM</td>
        <td>
          LocationId: 22113852498
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:37 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:37 AM</td>
        <td>
          Username: flsnfizhh1629, Password: 8qnyvaji (encrypted: 0/7GOCq0dOidM4gc9POETQ==), SystemName: auto_qa_sszizipmmf, UserFirstName: Fpdsudgn, UserLastName: Lsnfizhh, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:37 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:40 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fpdsudgn","userLastName":"Lsnfizhh","username":"flsnfizhh1629","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_sszizipmmf","practiceUsername":"op37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:40 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:40 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:46 AM</td>
        <td>
          Generated practiceUsername is: nx3789 and vendorUsername: nnewvendor6605 and vendorPassword: 39on0h6t
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:47 AM</td>
        <td>
          practiceLevelId(organizationId): 22124830963 and practiceId: 22320066882 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:47 AM</td>
        <td>
          LocationId: 22113852499
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:48 AM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:48 AM</td>
        <td>
          Username: flbxhdaqo1009, Password: eh1a4mtc (encrypted: XOmCUj7+JaqXgnQO71KJxA==), SystemName: auto_qa_zysgnryvtl, UserFirstName: Fwvyubte, UserLastName: Lbxhdaqo, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:49 AM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:51 AM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fwvyubte","userLastName":"Lbxhdaqo","username":"flbxhdaqo1009","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_zysgnryvtl","practiceUsername":"nx3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:51 AM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>11:59:51 AM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:01 PM</td>
        <td>
          Generated practiceUsername is: jc37892 and vendorUsername: nnewvendor9339 and vendorPassword: nqjjpyvy
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:02 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830964 and practiceId: 22320066912 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:02 PM</td>
        <td>
          LocationId: 22113852500
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:03 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:03 PM</td>
        <td>
          Username: fljajdyvi1897, Password: yc8csj7t (encrypted: m1FJ1RYW90w3e45LSkdw1A==), SystemName: auto_qa_rdkcujelzq, UserFirstName: Fuwlnrzp, UserLastName: Ljajdyvi, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:04 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:06 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fuwlnrzp","userLastName":"Ljajdyvi","username":"fljajdyvi1897","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rdkcujelzq","practiceUsername":"jc37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:06 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:06 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:11 PM</td>
        <td>
          Generated practiceUsername is: dm3789 and vendorUsername: nnewvendor8140 and vendorPassword: a43z2wb0
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:11 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830965 and practiceId: 22320066942 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:11 PM</td>
        <td>
          LocationId: 22113852501
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:13 PM</td>
        <td>
          Username: fljkfkokg1696, Password: u03jr022 (encrypted: RRhqx+qUx0O00XGvtzBk3Q==), SystemName: auto_qa_wwccxsmxme, UserFirstName: Frdpasfm, UserLastName: Ljkfkokg, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:14 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Frdpasfm","userLastName":"Ljkfkokg","username":"fljkfkokg1696","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_wwccxsmxme","practiceUsername":"dm3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:20 PM</td>
        <td>
          Generated practiceUsername is: vk3789 and vendorUsername: nnewvendor2984 and vendorPassword: 6b3cz8x8
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:21 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830966 and practiceId: 22320066972 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:21 PM</td>
        <td>
          LocationId: 22113852502
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:22 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:22 PM</td>
        <td>
          Username: florfgzdu1948, Password: 3zg6sbnn (encrypted: QX31jDBNIyI47/GWxJfSPA==), SystemName: auto_qa_poqrowpcgg, UserFirstName: Fcgdzqjq, UserLastName: Lorfgzdu, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:23 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:25 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fcgdzqjq","userLastName":"Lorfgzdu","username":"florfgzdu1948","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_poqrowpcgg","practiceUsername":"vk3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:25 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:25 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:30 PM</td>
        <td>
          Generated practiceUsername is: et37892 and vendorUsername: nnewvendor3331 and vendorPassword: de8bobjp
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:30 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830967 and practiceId: 22320067002 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:30 PM</td>
        <td>
          LocationId: 22113852503
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:32 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:32 PM</td>
        <td>
          Username: flzpfhnph1783, Password: 4yrokqa8 (encrypted: G+V+wQb5NNgIKId4Gs/IYA==), SystemName: auto_qa_gnemxjtetf, UserFirstName: Fshrexmq, UserLastName: Lzpfhnph, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:32 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:35 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fshrexmq","userLastName":"Lzpfhnph","username":"flzpfhnph1783","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_gnemxjtetf","practiceUsername":"et37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:35 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:35 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:40 PM</td>
        <td>
          Generated practiceUsername is: oo37891 and vendorUsername: nnewvendor5657 and vendorPassword: edvonk2e
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:40 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830968 and practiceId: 22320067032 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:40 PM</td>
        <td>
          LocationId: 22113852504
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:41 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:42 PM</td>
        <td>
          Username: flasncazb1412, Password: hphkqpi3 (encrypted: vWkJqRXP753/xPl1sMNVPA==), SystemName: auto_qa_jnejysdqzm, UserFirstName: Fizowcai, UserLastName: Lasncazb, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:42 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:45 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fizowcai","userLastName":"Lasncazb","username":"flasncazb1412","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jnejysdqzm","practiceUsername":"oo37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:45 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:45 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:50 PM</td>
        <td>
          Generated practiceUsername is: hi37891 and vendorUsername: nnewvendor13161 and vendorPassword: izt27o5j
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:51 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830969 and practiceId: 22320067062 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:51 PM</td>
        <td>
          LocationId: 22113852505
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:52 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:52 PM</td>
        <td>
          Username: flybxwkrd1064, Password: syi3q6ch (encrypted: kSAn1SdM2jk49wCt4hCFpw==), SystemName: auto_qa_yxosjjkzwj, UserFirstName: Fbbyoaie, UserLastName: Lybxwkrd, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:52 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:55 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fbbyoaie","userLastName":"Lybxwkrd","username":"flybxwkrd1064","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_yxosjjkzwj","practiceUsername":"hi37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:55 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:55 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:59 PM</td>
        <td>
          Generated practiceUsername is: gr3789 and vendorUsername: nnewvendor3517 and vendorPassword: ns8iwwx6
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:59 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830970 and practiceId: 22320067092 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:00:59 PM</td>
        <td>
          LocationId: 22113852506
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:00 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:01 PM</td>
        <td>
          Username: flitkknru1420, Password: 6q52e9fm (encrypted: zuEcMkhdc+WrNr5Hl1/GVg==), SystemName: auto_qa_klmebnzgew, UserFirstName: Fxywqliz, UserLastName: Litkknru, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:01 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:04 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fxywqliz","userLastName":"Litkknru","username":"flitkknru1420","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_klmebnzgew","practiceUsername":"gr3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:04 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:04 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:09 PM</td>
        <td>
          Generated practiceUsername is: li37893 and vendorUsername: nnewvendor8701 and vendorPassword: libiwecm
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:10 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830971 and practiceId: 22320067122 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:10 PM</td>
        <td>
          LocationId: 22113852507
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:11 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:11 PM</td>
        <td>
          Username: flcpemifa1793, Password: fpt6b6ho (encrypted: 9b1QVdQQPsAofP4ZXu51iQ==), SystemName: auto_qa_vbsitgijdh, UserFirstName: Fjqtbjhp, UserLastName: Lcpemifa, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:12 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:14 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fjqtbjhp","userLastName":"Lcpemifa","username":"flcpemifa1793","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_vbsitgijdh","practiceUsername":"li37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:14 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:14 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:18 PM</td>
        <td>
          Generated practiceUsername is: zm37891 and vendorUsername: nnewvendor9282 and vendorPassword: daydtzpk
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:19 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830972 and practiceId: 22320067152 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:19 PM</td>
        <td>
          LocationId: 22113852508
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:20 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:20 PM</td>
        <td>
          Username: flfxpuhyb1951, Password: u9aq87cq (encrypted: dUhZ6nMScO16swMq+bcWng==), SystemName: auto_qa_xaszuwzuzw, UserFirstName: Faplzdhw, UserLastName: Lfxpuhyb, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:21 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:23 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Faplzdhw","userLastName":"Lfxpuhyb","username":"flfxpuhyb1951","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_xaszuwzuzw","practiceUsername":"zm37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:23 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:23 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:29 PM</td>
        <td>
          Generated practiceUsername is: ez37893 and vendorUsername: nnewvendor3896 and vendorPassword: t8av4ydq
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:29 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830973 and practiceId: 22320067182 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:29 PM</td>
        <td>
          LocationId: 22113852509
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:31 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:31 PM</td>
        <td>
          Username: fljsbbugm1851, Password: okagbv29 (encrypted: 3klM+bys1jp3RrP6FpuOlA==), SystemName: auto_qa_ltwtaulhgz, UserFirstName: Fskqyvyr, UserLastName: Ljsbbugm, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:32 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:34 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fskqyvyr","userLastName":"Ljsbbugm","username":"fljsbbugm1851","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ltwtaulhgz","practiceUsername":"ez37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:34 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:34 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:38 PM</td>
        <td>
          Generated practiceUsername is: ml3789 and vendorUsername: nnewvendor3951 and vendorPassword: wr6v65f3
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:39 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830974 and practiceId: 22320067212 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:39 PM</td>
        <td>
          LocationId: 22113852510
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:40 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:40 PM</td>
        <td>
          Username: flgcsatho1092, Password: exy18oo0 (encrypted: aciL3SdqxawSyD8FOOuI0A==), SystemName: auto_qa_qkkrnmtkix, UserFirstName: Faobcwph, UserLastName: Lgcsatho, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:41 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:43 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Faobcwph","userLastName":"Lgcsatho","username":"flgcsatho1092","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qkkrnmtkix","practiceUsername":"ml3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:43 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:43 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:47 PM</td>
        <td>
          Generated practiceUsername is: un3789 and vendorUsername: nnewvendor1595 and vendorPassword: eqcdkrap
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:48 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830975 and practiceId: 22320067242 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:48 PM</td>
        <td>
          LocationId: 22113852511
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:49 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:50 PM</td>
        <td>
          Username: fliqpbpef1606, Password: l2ma5p45 (encrypted: +CSUsQ89AINw92GF8iJPzA==), SystemName: auto_qa_qtaduiaxnp, UserFirstName: Fabivzka, UserLastName: Liqpbpef, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:50 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:53 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fabivzka","userLastName":"Liqpbpef","username":"fliqpbpef1606","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qtaduiaxnp","practiceUsername":"un3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:53 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:53 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:57 PM</td>
        <td>
          Generated practiceUsername is: pp37892 and vendorUsername: nnewvendor8788 and vendorPassword: vfajzy4b
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:58 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830976 and practiceId: 22320067272 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:58 PM</td>
        <td>
          LocationId: 22113852512
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:59 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:59 PM</td>
        <td>
          Username: flmtdtvuz1868, Password: vp71u09t (encrypted: HJAA74SHvFJNQn3Zs2lS8Q==), SystemName: auto_qa_piizwcrvvq, UserFirstName: Fhnvgphe, UserLastName: Lmtdtvuz, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:01:59 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:02 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhnvgphe","userLastName":"Lmtdtvuz","username":"flmtdtvuz1868","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_piizwcrvvq","practiceUsername":"pp37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:02 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:02 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:08 PM</td>
        <td>
          Generated practiceUsername is: is37892 and vendorUsername: nnewvendor9507 and vendorPassword: pmsx78q5
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:08 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830977 and practiceId: 22320067302 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:08 PM</td>
        <td>
          LocationId: 22113852513
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:09 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:10 PM</td>
        <td>
          Username: flzsujsrd1892, Password: hap0deb0 (encrypted: Cb60n39yhYc9GQSi9em3Ow==), SystemName: auto_qa_zpxenbsoyi, UserFirstName: Fqjfxhfa, UserLastName: Lzsujsrd, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:10 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:13 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fqjfxhfa","userLastName":"Lzsujsrd","username":"flzsujsrd1892","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_zpxenbsoyi","practiceUsername":"is37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:13 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:13 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:18 PM</td>
        <td>
          Generated practiceUsername is: qu3789 and vendorUsername: nnewvendor6343 and vendorPassword: b9td9tpw
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:19 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830978 and practiceId: 22320067332 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:19 PM</td>
        <td>
          LocationId: 22113852514
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:21 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:21 PM</td>
        <td>
          Username: flstigirk1060, Password: kbxkdd5r (encrypted: Zr/pybUdoJKJUH0JNtc+yA==), SystemName: auto_qa_diztovslgm, UserFirstName: Fvyecena, UserLastName: Lstigirk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:22 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:24 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fvyecena","userLastName":"Lstigirk","username":"flstigirk1060","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_diztovslgm","practiceUsername":"qu3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:24 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:24 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:30 PM</td>
        <td>
          Generated practiceUsername is: zy3789 and vendorUsername: nnewvendor1266 and vendorPassword: 1f54mfam
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:31 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830979 and practiceId: 22320067362 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:31 PM</td>
        <td>
          LocationId: 22113852515
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:32 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:32 PM</td>
        <td>
          Username: flswsfmgf1375, Password: 01r4qu5y (encrypted: iKhtzoiCfQzBXz6CQB7j7A==), SystemName: auto_qa_utfypffvlk, UserFirstName: Fmhdmrik, UserLastName: Lswsfmgf, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:33 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:35 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmhdmrik","userLastName":"Lswsfmgf","username":"flswsfmgf1375","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_utfypffvlk","practiceUsername":"zy3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:35 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:35 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:43 PM</td>
        <td>
          Generated practiceUsername is: zf3789 and vendorUsername: nnewvendor75321 and vendorPassword: uyhgw896
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:43 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830980 and practiceId: 22320067392 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:43 PM</td>
        <td>
          LocationId: 22113852516
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:45 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:45 PM</td>
        <td>
          Username: flnatbyjw1845, Password: a7vgozxy (encrypted: lAwl5TXXTmIvj3cpG0PCXg==), SystemName: auto_qa_fjkheienfy, UserFirstName: Fitbbinp, UserLastName: Lnatbyjw, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:46 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:48 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fitbbinp","userLastName":"Lnatbyjw","username":"flnatbyjw1845","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_fjkheienfy","practiceUsername":"zf3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:48 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:02:48 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:10 PM</td>
        <td>
          Generated practiceUsername is: jy378952 and vendorUsername: nnewvendor4068 and vendorPassword: wu5sdr52
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:10 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830981 and practiceId: 22320067422 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:10 PM</td>
        <td>
          LocationId: 22113852517
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:12 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:12 PM</td>
        <td>
          Username: flmaytbxf1802, Password: 5pgupu8n (encrypted: 8lyK8vQs9uuNqtppbBAVXw==), SystemName: auto_qa_jgkkhrqxye, UserFirstName: Feitwfkn, UserLastName: Lmaytbxf, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:13 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:15 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Feitwfkn","userLastName":"Lmaytbxf","username":"flmaytbxf1802","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jgkkhrqxye","practiceUsername":"jy378952","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:15 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:15 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:23 PM</td>
        <td>
          Generated practiceUsername is: tl37891 and vendorUsername: nnewvendor3083 and vendorPassword: vaj4e0ps
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:24 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830982 and practiceId: 22320067452 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:24 PM</td>
        <td>
          LocationId: 22113852518
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:26 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:26 PM</td>
        <td>
          Username: flbawsokk1952, Password: vo616c7y (encrypted: dxNE9bfZwqX7bvHYq0PHSw==), SystemName: auto_qa_ihtlpygerk, UserFirstName: Fasigglp, UserLastName: Lbawsokk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:27 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:29 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fasigglp","userLastName":"Lbawsokk","username":"flbawsokk1952","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ihtlpygerk","practiceUsername":"tl37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:29 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:29 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:34 PM</td>
        <td>
          Generated practiceUsername is: jz37891 and vendorUsername: nnewvendor63052 and vendorPassword: flolzjmb
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:35 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830983 and practiceId: 22320067482 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:35 PM</td>
        <td>
          LocationId: 22113852519
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:36 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:36 PM</td>
        <td>
          Username: flzbhrpqa1616, Password: fgluvt4z (encrypted: gv0Yt6IvwqoHcHcYiI5huA==), SystemName: auto_qa_coqvgwkbqq, UserFirstName: Fusgxhvi, UserLastName: Lzbhrpqa, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:37 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:39 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fusgxhvi","userLastName":"Lzbhrpqa","username":"flzbhrpqa1616","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_coqvgwkbqq","practiceUsername":"jz37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:39 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:39 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:43 PM</td>
        <td>
          Generated practiceUsername is: pq37891 and vendorUsername: nnewvendor9235 and vendorPassword: sodcp6ab
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:44 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830984 and practiceId: 22320067512 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:44 PM</td>
        <td>
          LocationId: 22113852520
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:45 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:45 PM</td>
        <td>
          Username: flrprsfki1810, Password: flqza109 (encrypted: oFn4sltvfWM+ufjDp4SO2A==), SystemName: auto_qa_rylaacibxv, UserFirstName: Fnsonume, UserLastName: Lrprsfki, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:46 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:48 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fnsonume","userLastName":"Lrprsfki","username":"flrprsfki1810","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rylaacibxv","practiceUsername":"pq37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:48 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:48 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:52 PM</td>
        <td>
          Generated practiceUsername is: it37891 and vendorUsername: nnewvendor1142 and vendorPassword: c2i44nlr
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:53 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830985 and practiceId: 22320067542 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:53 PM</td>
        <td>
          LocationId: 22113852521
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:54 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:54 PM</td>
        <td>
          Username: flzqinqti1298, Password: wz7xqnaa (encrypted: 6UDCEEoTkhpyW3I6qpcG7g==), SystemName: auto_qa_dohcitytpt, UserFirstName: Ffnxdzjr, UserLastName: Lzqinqti, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:55 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:57 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ffnxdzjr","userLastName":"Lzqinqti","username":"flzqinqti1298","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_dohcitytpt","practiceUsername":"it37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:57 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:03:57 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:01 PM</td>
        <td>
          Generated practiceUsername is: bl37891 and vendorUsername: nnewvendor1228 and vendorPassword: 1i6tsaog
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:01 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830986 and practiceId: 22320067572 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:01 PM</td>
        <td>
          LocationId: 22113852522
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:02 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:03 PM</td>
        <td>
          Username: flsuxdhab1230, Password: 14odcmjz (encrypted: F8DsqHEiLolt7Z7fTMkIcQ==), SystemName: auto_qa_wisgzykate, UserFirstName: Ftlcodcn, UserLastName: Lsuxdhab, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:03 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:05 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ftlcodcn","userLastName":"Lsuxdhab","username":"flsuxdhab1230","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_wisgzykate","practiceUsername":"bl37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:05 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:05 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:11 PM</td>
        <td>
          Generated practiceUsername is: te37894 and vendorUsername: nnewvendor9150 and vendorPassword: ynbzfdwx
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:11 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830987 and practiceId: 22320067602 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:11 PM</td>
        <td>
          LocationId: 22113852523
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:12 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:13 PM</td>
        <td>
          Username: flveygfer1532, Password: 02zwpv6n (encrypted: UmBCEwualEziJldbjyqQSA==), SystemName: auto_qa_nhtnugfjps, UserFirstName: Fuyfyfqu, UserLastName: Lveygfer, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:13 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:17 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fuyfyfqu","userLastName":"Lveygfer","username":"flveygfer1532","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_nhtnugfjps","practiceUsername":"te37894","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:17 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:17 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:21 PM</td>
        <td>
          Generated practiceUsername is: rb3789 and vendorUsername: nnewvendor7413 and vendorPassword: i7q5la6a
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:22 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830988 and practiceId: 22320067632 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:22 PM</td>
        <td>
          LocationId: 22113852524
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:23 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:23 PM</td>
        <td>
          Username: fljgotelb1025, Password: ezle19pz (encrypted: xTiloOaqhsnRWXa3mws+pQ==), SystemName: auto_qa_qfavodkwkj, UserFirstName: Fdvwfsuv, UserLastName: Ljgotelb, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:24 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:26 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fdvwfsuv","userLastName":"Ljgotelb","username":"fljgotelb1025","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qfavodkwkj","practiceUsername":"rb3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:26 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:26 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:31 PM</td>
        <td>
          Generated practiceUsername is: vu37892 and vendorUsername: nnewvendor57015 and vendorPassword: 444i5o0v
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:32 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830989 and practiceId: 22320067662 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:32 PM</td>
        <td>
          LocationId: 22113852525
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:33 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:33 PM</td>
        <td>
          Username: fljxvrose1290, Password: hqua6dn5 (encrypted: 98EfRLfClavwBiwm3f+HVQ==), SystemName: auto_qa_jhkyyvwnur, UserFirstName: Fhnsjcat, UserLastName: Ljxvrose, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:34 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:36 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhnsjcat","userLastName":"Ljxvrose","username":"fljxvrose1290","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jhkyyvwnur","practiceUsername":"vu37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:36 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:36 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:41 PM</td>
        <td>
          Generated practiceUsername is: tz37891 and vendorUsername: nnewvendor8740 and vendorPassword: 57a8dwkt
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:41 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830990 and practiceId: 22320067692 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:41 PM</td>
        <td>
          LocationId: 22113852526
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:43 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:43 PM</td>
        <td>
          Username: flzdizkbc1950, Password: q133vnov (encrypted: TAS1Oo4yxjPSJlECDPdjRA==), SystemName: auto_qa_jotjziojdn, UserFirstName: Fvnmwbtp, UserLastName: Lzdizkbc, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:43 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:45 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fvnmwbtp","userLastName":"Lzdizkbc","username":"flzdizkbc1950","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jotjziojdn","practiceUsername":"tz37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:45 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:46 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:51 PM</td>
        <td>
          Generated practiceUsername is: dz3789 and vendorUsername: nnewvendor1652 and vendorPassword: jng90238
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:52 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830991 and practiceId: 22320067722 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:52 PM</td>
        <td>
          LocationId: 22113852527
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:53 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:53 PM</td>
        <td>
          Username: flsuppsxs1657, Password: 41xn37wp (encrypted: GOmVS3oa0cq/1E8hrBWf6w==), SystemName: auto_qa_cesendoyly, UserFirstName: Fabsafst, UserLastName: Lsuppsxs, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:54 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:56 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fabsafst","userLastName":"Lsuppsxs","username":"flsuppsxs1657","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_cesendoyly","practiceUsername":"dz3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:56 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:04:56 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:02 PM</td>
        <td>
          Generated practiceUsername is: bx3789 and vendorUsername: nnewvendor9529 and vendorPassword: 3taek8v0
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:03 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830992 and practiceId: 22320067752 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:03 PM</td>
        <td>
          LocationId: 22113852528
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:04 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:04 PM</td>
        <td>
          Username: flznoehyl1439, Password: wo1hubd1 (encrypted: Ep7hfVT8ZjsrhK+Z7DKiVg==), SystemName: auto_qa_tivzhscqul, UserFirstName: Fjxoqaxd, UserLastName: Lznoehyl, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:05 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:07 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fjxoqaxd","userLastName":"Lznoehyl","username":"flznoehyl1439","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_tivzhscqul","practiceUsername":"bx3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:07 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:07 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:12 PM</td>
        <td>
          Generated practiceUsername is: wk37891 and vendorUsername: nnewvendor1576 and vendorPassword: ljfdyho3
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:12 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830993 and practiceId: 22320067782 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:12 PM</td>
        <td>
          LocationId: 22113852529
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:14 PM</td>
        <td>
          Username: flhcirboi1430, Password: zr5wtyhj (encrypted: iW5+7RqSfymFKuRe97bpPg==), SystemName: auto_qa_ybzqiavehq, UserFirstName: Fpmqrolk, UserLastName: Lhcirboi, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:14 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fpmqrolk","userLastName":"Lhcirboi","username":"flhcirboi1430","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ybzqiavehq","practiceUsername":"wk37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:22 PM</td>
        <td>
          Generated practiceUsername is: om3789 and vendorUsername: nnewvendor46516 and vendorPassword: tloz8g46
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:22 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830994 and practiceId: 22320067812 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:22 PM</td>
        <td>
          LocationId: 22113852530
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:24 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:24 PM</td>
        <td>
          Username: flmkivlsw1833, Password: dv56y30u (encrypted: 6545vahruQnOQvn8gjXUUg==), SystemName: auto_qa_ildeclrufk, UserFirstName: Fmskezrc, UserLastName: Lmkivlsw, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:24 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:27 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmskezrc","userLastName":"Lmkivlsw","username":"flmkivlsw1833","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ildeclrufk","practiceUsername":"om3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:27 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:27 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:32 PM</td>
        <td>
          Generated practiceUsername is: sp37891 and vendorUsername: nnewvendor5166 and vendorPassword: fr5pjcit
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:32 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830995 and practiceId: 22320067842 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:32 PM</td>
        <td>
          LocationId: 22113852531
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:34 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:34 PM</td>
        <td>
          Username: flinhgoxl1517, Password: qbv5nvfg (encrypted: JgtCDEn8eIZRU7wrmU+d/w==), SystemName: auto_qa_aeuiwmhcal, UserFirstName: Foubkuan, UserLastName: Linhgoxl, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:34 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:38 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Foubkuan","userLastName":"Linhgoxl","username":"flinhgoxl1517","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_aeuiwmhcal","practiceUsername":"sp37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:38 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:38 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:44 PM</td>
        <td>
          Generated practiceUsername is: ax3789 and vendorUsername: nnewvendor2442 and vendorPassword: bv4gtmvd
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:45 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830996 and practiceId: 22320067872 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:45 PM</td>
        <td>
          LocationId: 22113852532
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:46 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:46 PM</td>
        <td>
          Username: floagkduu1322, Password: tdd55ia0 (encrypted: IdLKylzVJEktEY13q+LJeQ==), SystemName: auto_qa_meqwjcuybm, UserFirstName: Fxvqwhbp, UserLastName: Loagkduu, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:47 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:49 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fxvqwhbp","userLastName":"Loagkduu","username":"floagkduu1322","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_meqwjcuybm","practiceUsername":"ax3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:49 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:49 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:55 PM</td>
        <td>
          Generated practiceUsername is: uk37891 and vendorUsername: nnewvendor6809 and vendorPassword: jlmqepio
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:56 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830997 and practiceId: 22320067902 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:56 PM</td>
        <td>
          LocationId: 22113852533
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:57 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:57 PM</td>
        <td>
          Username: flzrkdfin1339, Password: cpo206oj (encrypted: SZMVd5zOkumneXZT4FEIZA==), SystemName: auto_qa_mqduruwlip, UserFirstName: Fjtojitg, UserLastName: Lzrkdfin, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:05:58 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:00 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fjtojitg","userLastName":"Lzrkdfin","username":"flzrkdfin1339","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_mqduruwlip","practiceUsername":"uk37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:00 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:00 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:05 PM</td>
        <td>
          Generated practiceUsername is: rt37892 and vendorUsername: nnewvendor4014 and vendorPassword: iyd3us0m
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:06 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830998 and practiceId: 22320067932 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:06 PM</td>
        <td>
          LocationId: 22113852534
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:07 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:07 PM</td>
        <td>
          Username: flgypgngn1746, Password: cft8hk72 (encrypted: Nqb7Gpl84tj2HsrG3zCRvg==), SystemName: auto_qa_kgdfdjlddv, UserFirstName: Fdzeutml, UserLastName: Lgypgngn, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:08 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:10 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fdzeutml","userLastName":"Lgypgngn","username":"flgypgngn1746","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_kgdfdjlddv","practiceUsername":"rt37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:10 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:10 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:15 PM</td>
        <td>
          Generated practiceUsername is: hu37893 and vendorUsername: nnewvendor7924 and vendorPassword: qappf08k
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:16 PM</td>
        <td>
          practiceLevelId(organizationId): 22124830999 and practiceId: 22320067962 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:16 PM</td>
        <td>
          LocationId: 22113852535
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:18 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:18 PM</td>
        <td>
          Username: flgwiimzu1636, Password: mpvwb1mb (encrypted: DYzlAsm1Y1cHqT+iA+zHog==), SystemName: auto_qa_alzkktxxow, UserFirstName: Fafxcxbp, UserLastName: Lgwiimzu, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:19 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:21 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fafxcxbp","userLastName":"Lgwiimzu","username":"flgwiimzu1636","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_alzkktxxow","practiceUsername":"hu37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:21 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:21 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:26 PM</td>
        <td>
          Generated practiceUsername is: lt3789 and vendorUsername: nnewvendor1416 and vendorPassword: n1pwyidl
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:26 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831000 and practiceId: 22320067992 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:26 PM</td>
        <td>
          LocationId: 22113852536
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:28 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:28 PM</td>
        <td>
          Username: flccsleis1193, Password: 6j4i197q (encrypted: MZ8I5kXO3TUy9dttMk5ZKQ==), SystemName: auto_qa_ezrfncvrab, UserFirstName: Fleuitoj, UserLastName: Lccsleis, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:28 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:31 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fleuitoj","userLastName":"Lccsleis","username":"flccsleis1193","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ezrfncvrab","practiceUsername":"lt3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:31 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:31 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:35 PM</td>
        <td>
          Generated practiceUsername is: ui37891 and vendorUsername: nnewvendor9371 and vendorPassword: ov4owdyb
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:36 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831001 and practiceId: 22320068022 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:36 PM</td>
        <td>
          LocationId: 22113852537
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:37 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:37 PM</td>
        <td>
          Username: fllbsywtt1462, Password: wzr72unb (encrypted: AFT2n0GHQkr0NWVHRSA6UA==), SystemName: auto_qa_rsezsmoqlw, UserFirstName: Friufgly, UserLastName: Llbsywtt, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:38 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:40 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Friufgly","userLastName":"Llbsywtt","username":"fllbsywtt1462","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rsezsmoqlw","practiceUsername":"ui37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:40 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:40 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:44 PM</td>
        <td>
          Generated practiceUsername is: rn3789 and vendorUsername: nnewvendor67012 and vendorPassword: 1s8pe83y
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:45 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831002 and practiceId: 22320068052 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:45 PM</td>
        <td>
          LocationId: 22113852538
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:46 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:46 PM</td>
        <td>
          Username: flyikwzjk1514, Password: jtcjlefh (encrypted: g8O4zveuvCFTYof4jnQNGw==), SystemName: auto_qa_wpjitcbyiq, UserFirstName: Fijqavnr, UserLastName: Lyikwzjk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:47 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:49 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fijqavnr","userLastName":"Lyikwzjk","username":"flyikwzjk1514","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_wpjitcbyiq","practiceUsername":"rn3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:49 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:49 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:54 PM</td>
        <td>
          Generated practiceUsername is: nn37891 and vendorUsername: nnewvendor6753 and vendorPassword: bhlhzzfi
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:54 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831003 and practiceId: 22320068082 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:54 PM</td>
        <td>
          LocationId: 22113852539
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:55 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:56 PM</td>
        <td>
          Username: fljhvbhuh1343, Password: zibsvkgj (encrypted: E9251oIRaSVKUqd+30ZmCg==), SystemName: auto_qa_xzdhgjpbuc, UserFirstName: Fealkire, UserLastName: Ljhvbhuh, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:56 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:58 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fealkire","userLastName":"Ljhvbhuh","username":"fljhvbhuh1343","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_xzdhgjpbuc","practiceUsername":"nn37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:58 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:06:58 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:03 PM</td>
        <td>
          Generated practiceUsername is: je3789 and vendorUsername: nnewvendor1081 and vendorPassword: pk8sy5mt
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:03 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831004 and practiceId: 22320068112 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:03 PM</td>
        <td>
          LocationId: 22113852540
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:04 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:04 PM</td>
        <td>
          Username: flhwohsmk1075, Password: camsrf38 (encrypted: kt2bpPUkyQs97nmKShluPg==), SystemName: auto_qa_rzaptcvyia, UserFirstName: Frrtninb, UserLastName: Lhwohsmk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:05 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:07 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Frrtninb","userLastName":"Lhwohsmk","username":"flhwohsmk1075","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rzaptcvyia","practiceUsername":"je3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:07 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:07 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:12 PM</td>
        <td>
          Generated practiceUsername is: qe37891 and vendorUsername: nnewvendor8104 and vendorPassword: bkdzct44
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:12 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831005 and practiceId: 22320068142 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:12 PM</td>
        <td>
          LocationId: 22113852541
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:14 PM</td>
        <td>
          Username: flzqknebk1752, Password: qj9o5uex (encrypted: NeweChWHHg85/1jol6Yehw==), SystemName: auto_qa_rrpvhvytgo, UserFirstName: Fqnpavtq, UserLastName: Lzqknebk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:14 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fqnpavtq","userLastName":"Lzqknebk","username":"flzqknebk1752","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_rrpvhvytgo","practiceUsername":"qe37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:21 PM</td>
        <td>
          Generated practiceUsername is: ud3789 and vendorUsername: nnewvendor8250 and vendorPassword: m7zq8s1y
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:21 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831006 and practiceId: 22320068172 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:21 PM</td>
        <td>
          LocationId: 22113852542
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:22 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:23 PM</td>
        <td>
          Username: flgahkukj1808, Password: q0bqjv17 (encrypted: bs1vg7aRjTuIzaqNoq50pw==), SystemName: auto_qa_ahcyfppcea, UserFirstName: Fizvmzjy, UserLastName: Lgahkukj, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:23 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:25 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fizvmzjy","userLastName":"Lgahkukj","username":"flgahkukj1808","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ahcyfppcea","practiceUsername":"ud3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:25 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:25 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:32 PM</td>
        <td>
          Generated practiceUsername is: ar37892 and vendorUsername: nnewvendor5231 and vendorPassword: kvu2sb7f
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:33 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831007 and practiceId: 22320068202 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:33 PM</td>
        <td>
          LocationId: 22113852543
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:34 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:34 PM</td>
        <td>
          Username: flfojizmc1283, Password: g7uhipaz (encrypted: ch1SxaoVNlLGvn8lObtU0w==), SystemName: auto_qa_jedufiblvv, UserFirstName: Fgqpncka, UserLastName: Lfojizmc, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:35 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:37 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fgqpncka","userLastName":"Lfojizmc","username":"flfojizmc1283","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jedufiblvv","practiceUsername":"ar37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:37 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:37 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:44 PM</td>
        <td>
          Generated practiceUsername is: hk37891 and vendorUsername: nnewvendor5359 and vendorPassword: 6r5cqza7
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:45 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831008 and practiceId: 22320068232 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:45 PM</td>
        <td>
          LocationId: 22113852544
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:46 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:46 PM</td>
        <td>
          Username: flfosoiwi1420, Password: kii07m1n (encrypted: 0Yw/HkrKtw/RA+wXNvV2fw==), SystemName: auto_qa_xxwgipcavx, UserFirstName: Fjaewcwq, UserLastName: Lfosoiwi, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:47 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:49 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fjaewcwq","userLastName":"Lfosoiwi","username":"flfosoiwi1420","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_xxwgipcavx","practiceUsername":"hk37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:49 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:49 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:56 PM</td>
        <td>
          Generated practiceUsername is: of37892 and vendorUsername: nnewvendor5591 and vendorPassword: qysefdws
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:56 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831009 and practiceId: 22320068262 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:56 PM</td>
        <td>
          LocationId: 22113852545
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:58 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:58 PM</td>
        <td>
          Username: flpanxwnm1969, Password: utrioib1 (encrypted: Ejv5A8EKM5PW+Woyf4U6fA==), SystemName: auto_qa_mlptmcsmzy, UserFirstName: Fhzwcrfi, UserLastName: Lpanxwnm, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:07:58 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:01 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhzwcrfi","userLastName":"Lpanxwnm","username":"flpanxwnm1969","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_mlptmcsmzy","practiceUsername":"of37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:01 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:01 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:07 PM</td>
        <td>
          Generated practiceUsername is: hl3789 and vendorUsername: nnewvendor9877 and vendorPassword: 7px7m3jc
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:07 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831010 and practiceId: 22320068292 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:07 PM</td>
        <td>
          LocationId: 22113852546
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:08 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:09 PM</td>
        <td>
          Username: flgkihrkn1492, Password: 7m9gze4i (encrypted: CqFUxhQeBIXSMabDsGZl4A==), SystemName: auto_qa_ovzebtnevg, UserFirstName: Ficcmsws, UserLastName: Lgkihrkn, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:09 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:12 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ficcmsws","userLastName":"Lgkihrkn","username":"flgkihrkn1492","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ovzebtnevg","practiceUsername":"hl3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:12 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:12 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:22 PM</td>
        <td>
          Generated practiceUsername is: ij37892 and vendorUsername: nnewvendor2238 and vendorPassword: nakvhlbt
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:22 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831011 and practiceId: 22320068322 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:22 PM</td>
        <td>
          LocationId: 22113852547
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:23 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:24 PM</td>
        <td>
          Username: flkpvmwhm1531, Password: z0ely9mm (encrypted: UJolqFYE8+prJSnDXNCuow==), SystemName: auto_qa_qabfeaetel, UserFirstName: Fahwvrnm, UserLastName: Lkpvmwhm, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:24 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:27 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fahwvrnm","userLastName":"Lkpvmwhm","username":"flkpvmwhm1531","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qabfeaetel","practiceUsername":"ij37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:27 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:27 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:31 PM</td>
        <td>
          Generated practiceUsername is: rn37891 and vendorUsername: nnewvendor6318 and vendorPassword: ovpl1yx6
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:32 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831012 and practiceId: 22320068352 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:32 PM</td>
        <td>
          LocationId: 22113852548
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:33 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:33 PM</td>
        <td>
          Username: flqplahuk1670, Password: d5pqkwg7 (encrypted: 2tacXqrQuOi0ruY+sBKRBQ==), SystemName: auto_qa_cyyitdhwkx, UserFirstName: Ffqanabe, UserLastName: Lqplahuk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:33 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:36 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ffqanabe","userLastName":"Lqplahuk","username":"flqplahuk1670","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_cyyitdhwkx","practiceUsername":"rn37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:36 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:36 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:43 PM</td>
        <td>
          Generated practiceUsername is: we378910 and vendorUsername: nnewvendor6594 and vendorPassword: 6tjocaf8
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:43 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831013 and practiceId: 22320068382 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:43 PM</td>
        <td>
          LocationId: 22113852549
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:44 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:45 PM</td>
        <td>
          Username: flozftmzy1845, Password: 6h4bqsvq (encrypted: lpd00nvhXooJwk9N1bbGsA==), SystemName: auto_qa_jwdgjxzoke, UserFirstName: Fcaenibx, UserLastName: Lozftmzy, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:45 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:47 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fcaenibx","userLastName":"Lozftmzy","username":"flozftmzy1845","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_jwdgjxzoke","practiceUsername":"we378910","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:47 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:47 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:52 PM</td>
        <td>
          Generated practiceUsername is: xp37893 and vendorUsername: nnewvendor4753 and vendorPassword: huqz0ufr
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:52 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831014 and practiceId: 22320068412 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:52 PM</td>
        <td>
          LocationId: 22113852550
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:54 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:54 PM</td>
        <td>
          Username: flgsribrl1652, Password: 43u0wmo7 (encrypted: Ckg6roKV5pCZTFlYnsRefw==), SystemName: auto_qa_fnbmfacdgy, UserFirstName: Fdxcfbfx, UserLastName: Lgsribrl, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:54 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:57 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fdxcfbfx","userLastName":"Lgsribrl","username":"flgsribrl1652","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_fnbmfacdgy","practiceUsername":"xp37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:57 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:08:57 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:02 PM</td>
        <td>
          Generated practiceUsername is: uw3789 and vendorUsername: nnewvendor5159 and vendorPassword: skypipdj
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:03 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831015 and practiceId: 22320068442 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:03 PM</td>
        <td>
          LocationId: 22113852551
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:04 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:04 PM</td>
        <td>
          Username: flwpyytcn1890, Password: zhemju19 (encrypted: xhrRJGhKmsjxpcVy2+plbQ==), SystemName: auto_qa_ojpvwzdmno, UserFirstName: Fehfgrus, UserLastName: Lwpyytcn, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:05 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:07 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fehfgrus","userLastName":"Lwpyytcn","username":"flwpyytcn1890","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ojpvwzdmno","practiceUsername":"uw3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:07 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:07 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:52 PM</td>
        <td>
          Generated practiceUsername is: ra3789153 and vendorUsername: nnewvendor3684 and vendorPassword: fobrv2jn
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:52 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831016 and practiceId: 22320068472 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:52 PM</td>
        <td>
          LocationId: 22113852552
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:54 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:54 PM</td>
        <td>
          Username: flafwjcjf1612, Password: 64s6rx4h (encrypted: dIrDM5XJkyq3rmw+G0/Iwg==), SystemName: auto_qa_bxdjzgcyqz, UserFirstName: Fyvqaqce, UserLastName: Lafwjcjf, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:55 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:57 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fyvqaqce","userLastName":"Lafwjcjf","username":"flafwjcjf1612","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_bxdjzgcyqz","practiceUsername":"ra3789153","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:57 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:09:57 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:18 PM</td>
        <td>
          Generated practiceUsername is: bf378951 and vendorUsername: nnewvendor7804 and vendorPassword: fcgw9fsr
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:18 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831017 and practiceId: 22320068502 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:18 PM</td>
        <td>
          LocationId: 22113852553
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:19 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:20 PM</td>
        <td>
          Username: fldgrfwji1543, Password: ati74h3k (encrypted: osLvtszroIpwz9lFu+/6qw==), SystemName: auto_qa_uvqbnynzot, UserFirstName: Ftawdxib, UserLastName: Ldgrfwji, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:20 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:23 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ftawdxib","userLastName":"Ldgrfwji","username":"fldgrfwji1543","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_uvqbnynzot","practiceUsername":"bf378951","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:23 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:23 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:27 PM</td>
        <td>
          Generated practiceUsername is: ht37892 and vendorUsername: nnewvendor3499 and vendorPassword: uwh5sgql
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:28 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831018 and practiceId: 22320068532 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:28 PM</td>
        <td>
          LocationId: 22113852554
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:29 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:29 PM</td>
        <td>
          Username: flqjtnhej1448, Password: exrq2cby (encrypted: qFJoLk7xYRkB4OPJBO0bEA==), SystemName: auto_qa_hesrcofadd, UserFirstName: Fobemqqg, UserLastName: Lqjtnhej, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:30 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:32 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fobemqqg","userLastName":"Lqjtnhej","username":"flqjtnhej1448","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_hesrcofadd","practiceUsername":"ht37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:32 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:32 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:37 PM</td>
        <td>
          Generated practiceUsername is: xe3789 and vendorUsername: nnewvendor2020 and vendorPassword: oi8p2mnb
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:37 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831019 and practiceId: 22320068562 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:37 PM</td>
        <td>
          LocationId: 22113852555
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:38 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:39 PM</td>
        <td>
          Username: flfrbyigx1473, Password: 0yhqqtjz (encrypted: amZj66XUlhTEpFqZo9jqmQ==), SystemName: auto_qa_hhtbwdhhlb, UserFirstName: Flfftsde, UserLastName: Lfrbyigx, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:39 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:41 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flfftsde","userLastName":"Lfrbyigx","username":"flfrbyigx1473","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_hhtbwdhhlb","practiceUsername":"xe3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:41 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:41 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:46 PM</td>
        <td>
          Generated practiceUsername is: ga37891 and vendorUsername: nnewvendor8450 and vendorPassword: patskhxy
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:47 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831020 and practiceId: 22320068592 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:47 PM</td>
        <td>
          LocationId: 22113852556
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:48 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:48 PM</td>
        <td>
          Username: flktohxga1698, Password: o91a8n2i (encrypted: haBaVGKI8CjJgRNg8yHCfQ==), SystemName: auto_qa_xbcvukwwxs, UserFirstName: Fjijgvev, UserLastName: Lktohxga, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:49 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:51 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fjijgvev","userLastName":"Lktohxga","username":"flktohxga1698","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_xbcvukwwxs","practiceUsername":"ga37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:51 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:51 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:58 PM</td>
        <td>
          Generated practiceUsername is: mi37894 and vendorUsername: nnewvendor50512 and vendorPassword: 57xuwmx0
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:59 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831021 and practiceId: 22320068622 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:10:59 PM</td>
        <td>
          LocationId: 22113852557
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:00 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:00 PM</td>
        <td>
          Username: flbojsguc1921, Password: wi5hs1ft (encrypted: qq8MpZaPeYFM+sxRSZgSRw==), SystemName: auto_qa_gbscqgjjrv, UserFirstName: Flzmkjyv, UserLastName: Lbojsguc, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:00 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:03 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flzmkjyv","userLastName":"Lbojsguc","username":"flbojsguc1921","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_gbscqgjjrv","practiceUsername":"mi37894","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:03 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:03 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:12 PM</td>
        <td>
          Generated practiceUsername is: ge378913 and vendorUsername: nnewvendor1870 and vendorPassword: ks882syu
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:12 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831022 and practiceId: 22320068652 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:12 PM</td>
        <td>
          LocationId: 22113852558
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:14 PM</td>
        <td>
          Username: flvqmuxdk1808, Password: 4ucvluo5 (encrypted: QM6ugaHFYWbs02GgCu8RQQ==), SystemName: auto_qa_skzkhvrfqp, UserFirstName: Fomqqpmg, UserLastName: Lvqmuxdk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:14 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fomqqpmg","userLastName":"Lvqmuxdk","username":"flvqmuxdk1808","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_skzkhvrfqp","practiceUsername":"ge378913","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:23 PM</td>
        <td>
          Generated practiceUsername is: cj37891 and vendorUsername: nnewvendor4914 and vendorPassword: x04n5oqt
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:23 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831023 and practiceId: 22320068682 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:23 PM</td>
        <td>
          LocationId: 22113852559
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:24 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:24 PM</td>
        <td>
          Username: flgxxzimb1081, Password: yoqjyt1g (encrypted: 1lCOa9JLvdcQSveQXojymg==), SystemName: auto_qa_urmwdvotrf, UserFirstName: Flvtnlcw, UserLastName: Lgxxzimb, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:25 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:27 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flvtnlcw","userLastName":"Lgxxzimb","username":"flgxxzimb1081","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_urmwdvotrf","practiceUsername":"cj37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:27 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:27 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:34 PM</td>
        <td>
          Generated practiceUsername is: mj37892 and vendorUsername: nnewvendor2633 and vendorPassword: hz15dtlc
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:34 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831024 and practiceId: 22320068712 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:34 PM</td>
        <td>
          LocationId: 22113852560
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:35 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:36 PM</td>
        <td>
          Username: flawfqvdq1552, Password: be9akcib (encrypted: CnVeo0A/knlpAghxUiit+w==), SystemName: auto_qa_btylahtbvs, UserFirstName: Feafgheo, UserLastName: Lawfqvdq, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:36 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:38 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Feafgheo","userLastName":"Lawfqvdq","username":"flawfqvdq1552","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_btylahtbvs","practiceUsername":"mj37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:38 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:38 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:45 PM</td>
        <td>
          Generated practiceUsername is: lx37892 and vendorUsername: nnewvendor1642 and vendorPassword: qpk15qug
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:46 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831025 and practiceId: 22320068742 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:46 PM</td>
        <td>
          LocationId: 22113852561
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:47 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:47 PM</td>
        <td>
          Username: flwvnmgqg1133, Password: wvkp62en (encrypted: G9rxEV73+VLfyRMVtiiAcw==), SystemName: auto_qa_sfgqxfrpgq, UserFirstName: Flqdqkfi, UserLastName: Lwvnmgqg, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:48 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:50 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flqdqkfi","userLastName":"Lwvnmgqg","username":"flwvnmgqg1133","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_sfgqxfrpgq","practiceUsername":"lx37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:50 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:50 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:57 PM</td>
        <td>
          Generated practiceUsername is: jx37891 and vendorUsername: nnewvendor4530 and vendorPassword: m6yw7n12
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:58 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831026 and practiceId: 22320068772 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:58 PM</td>
        <td>
          LocationId: 22113852562
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:59 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:59 PM</td>
        <td>
          Username: flvbqclfl1678, Password: oi31nw5s (encrypted: 9d5d6R8ELidMM68AAVMlVg==), SystemName: auto_qa_xkllvjezwz, UserFirstName: Fgpgdzce, UserLastName: Lvbqclfl, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:11:59 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:02 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fgpgdzce","userLastName":"Lvbqclfl","username":"flvbqclfl1678","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_xkllvjezwz","practiceUsername":"jx37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:02 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:02 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:11 PM</td>
        <td>
          Generated practiceUsername is: ka37893 and vendorUsername: nnewvendor5970 and vendorPassword: fb1fhuar
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:12 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831027 and practiceId: 22320068802 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:12 PM</td>
        <td>
          LocationId: 22113852563
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:13 PM</td>
        <td>
          Username: flshszshp1974, Password: 7mdt9fvo (encrypted: OomuqN6qFjyKnFKKso3BiQ==), SystemName: auto_qa_ektsmrtirq, UserFirstName: Ftkgkqyz, UserLastName: Lshszshp, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:14 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ftkgkqyz","userLastName":"Lshszshp","username":"flshszshp1974","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ektsmrtirq","practiceUsername":"ka37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:22 PM</td>
        <td>
          Generated practiceUsername is: tk37891 and vendorUsername: nnewvendor5316 and vendorPassword: l9ao48j8
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:23 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831028 and practiceId: 22320068832 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:23 PM</td>
        <td>
          LocationId: 22113852564
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:24 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:24 PM</td>
        <td>
          Username: fllzanxiq1741, Password: kgstt3vb (encrypted: WrTplKgnfHRpOXlxnlEhTg==), SystemName: auto_qa_pwddgrqtel, UserFirstName: Fludvhza, UserLastName: Llzanxiq, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:25 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:27 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fludvhza","userLastName":"Llzanxiq","username":"fllzanxiq1741","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_pwddgrqtel","practiceUsername":"tk37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:27 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:27 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:33 PM</td>
        <td>
          Generated practiceUsername is: zq3789 and vendorUsername: nnewvendor9017 and vendorPassword: kz1oaakh
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:33 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831029 and practiceId: 22320068862 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:33 PM</td>
        <td>
          LocationId: 22113852565
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:34 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:35 PM</td>
        <td>
          Username: flfldprcv1731, Password: ga202bz5 (encrypted: 04gVHuJXgDXjkmTk2a0BFA==), SystemName: auto_qa_amtpgohdnq, UserFirstName: Ftmzbxaw, UserLastName: Lfldprcv, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:35 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:37 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ftmzbxaw","userLastName":"Lfldprcv","username":"flfldprcv1731","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_amtpgohdnq","practiceUsername":"zq3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:37 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:37 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:43 PM</td>
        <td>
          Generated practiceUsername is: ec37891 and vendorUsername: nnewvendor5018 and vendorPassword: eneqk8gl
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:44 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831030 and practiceId: 22320068892 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:44 PM</td>
        <td>
          LocationId: 22113852566
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:45 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:45 PM</td>
        <td>
          Username: flzxljgul1758, Password: ffbg8aqy (encrypted: eKIW50BvV/zNf0nMKWLBUw==), SystemName: auto_qa_lvqtmeabzr, UserFirstName: Fndjyqul, UserLastName: Lzxljgul, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:46 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:48 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fndjyqul","userLastName":"Lzxljgul","username":"flzxljgul1758","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_lvqtmeabzr","practiceUsername":"ec37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:48 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:48 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:55 PM</td>
        <td>
          Generated practiceUsername is: cl37893 and vendorUsername: nnewvendor7729 and vendorPassword: sy38lrrb
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:55 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831031 and practiceId: 22320068922 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:55 PM</td>
        <td>
          LocationId: 22113852567
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:57 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:57 PM</td>
        <td>
          Username: flaaqrzkw1305, Password: j8tw5zcg (encrypted: oCqKuccqbRQtghyDxCPLqA==), SystemName: auto_qa_gvohldsuls, UserFirstName: Fxtneqyu, UserLastName: Laaqrzkw, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:57 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:59 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fxtneqyu","userLastName":"Laaqrzkw","username":"flaaqrzkw1305","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_gvohldsuls","practiceUsername":"cl37893","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:59 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:12:59 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:10 PM</td>
        <td>
          Generated practiceUsername is: ap3789 and vendorUsername: nnewvendor9237 and vendorPassword: qul4w4qf
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:10 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831032 and practiceId: 22320068952 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:10 PM</td>
        <td>
          LocationId: 22113852568
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:11 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:12 PM</td>
        <td>
          Username: flddpzjkb1353, Password: vhl81gqh (encrypted: 8nPrQhmiWDZU22Q9s9Smcw==), SystemName: auto_qa_qzslbusasv, UserFirstName: Fmwsibhc, UserLastName: Lddpzjkb, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:12 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:15 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmwsibhc","userLastName":"Lddpzjkb","username":"flddpzjkb1353","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_qzslbusasv","practiceUsername":"ap3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:15 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:15 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:22 PM</td>
        <td>
          Generated practiceUsername is: zv3789 and vendorUsername: nnewvendor1769 and vendorPassword: vvfsfi5k
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:22 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831033 and practiceId: 22320068982 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:22 PM</td>
        <td>
          LocationId: 22113852569
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:26 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:26 PM</td>
        <td>
          Username: fluiwxbot1632, Password: gf212j9r (encrypted: Hsp2hQQ8dWMmeAPyOZYfVw==), SystemName: auto_qa_fmvvvirfsb, UserFirstName: Fymqkvst, UserLastName: Luiwxbot, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:27 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:29 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fymqkvst","userLastName":"Luiwxbot","username":"fluiwxbot1632","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_fmvvvirfsb","practiceUsername":"zv3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:29 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:29 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:33 PM</td>
        <td>
          Generated practiceUsername is: wq37891 and vendorUsername: nnewvendor3039 and vendorPassword: n28695mv
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:34 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831034 and practiceId: 22320069012 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:34 PM</td>
        <td>
          LocationId: 22113852570
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:35 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:35 PM</td>
        <td>
          Username: flviqzzys1514, Password: sritwh77 (encrypted: C9gElVIzDODijLZGk/bBjw==), SystemName: auto_qa_fnehhdplrh, UserFirstName: Fxbkjhpj, UserLastName: Lviqzzys, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:36 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:39 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fxbkjhpj","userLastName":"Lviqzzys","username":"flviqzzys1514","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_fnehhdplrh","practiceUsername":"wq37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:39 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:39 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:44 PM</td>
        <td>
          Generated practiceUsername is: yw37891 and vendorUsername: nnewvendor5325 and vendorPassword: hcnr0bn9
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:45 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831035 and practiceId: 22320069042 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:45 PM</td>
        <td>
          LocationId: 22113852571
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:46 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:47 PM</td>
        <td>
          Username: flivtipdx1472, Password: t7cbvfrc (encrypted: j3VrG9DTCAjS7Q+thg6ZBQ==), SystemName: auto_qa_lkgsgncwmq, UserFirstName: Fhwkgotf, UserLastName: Livtipdx, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:47 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:51 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhwkgotf","userLastName":"Livtipdx","username":"flivtipdx1472","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_lkgsgncwmq","practiceUsername":"yw37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:51 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:51 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:56 PM</td>
        <td>
          Generated practiceUsername is: zt3789 and vendorUsername: nnewvendor3095 and vendorPassword: 1ekyl50e
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:57 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831036 and practiceId: 22320069072 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:57 PM</td>
        <td>
          LocationId: 22113852572
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:58 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:59 PM</td>
        <td>
          Username: flvrgjxdn1306, Password: 57uo2ppd (encrypted: pj1djNe66YayeU2u9sUt7A==), SystemName: auto_qa_cmbhtzzstu, UserFirstName: Flgoxpef, UserLastName: Lvrgjxdn, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:13:59 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:02 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flgoxpef","userLastName":"Lvrgjxdn","username":"flvrgjxdn1306","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_cmbhtzzstu","practiceUsername":"zt3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:02 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:02 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:07 PM</td>
        <td>
          Generated practiceUsername is: zi37892 and vendorUsername: nnewvendor1877 and vendorPassword: 1ibfdqy2
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:08 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831037 and practiceId: 22320069102 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:08 PM</td>
        <td>
          LocationId: 22113852573
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:09 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:09 PM</td>
        <td>
          Username: flerjbimy1335, Password: 1j4r74fi (encrypted: g4K6abSgOyugN7KVZrGPqw==), SystemName: auto_qa_yeewhsbnik, UserFirstName: Ffxahswo, UserLastName: Lerjbimy, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:10 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:13 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Ffxahswo","userLastName":"Lerjbimy","username":"flerjbimy1335","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_yeewhsbnik","practiceUsername":"zi37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:13 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:13 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:18 PM</td>
        <td>
          Generated practiceUsername is: aq37892 and vendorUsername: nnewvendor5644 and vendorPassword: z93fk4e5
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:19 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831038 and practiceId: 22320069132 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:19 PM</td>
        <td>
          LocationId: 22113852574
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:20 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:20 PM</td>
        <td>
          Username: fljhbidsw1481, Password: qv6dwqiw (encrypted: Y1OQkX2q8oy0aJQjuWd5bQ==), SystemName: auto_qa_mnpjlayiky, UserFirstName: Fnvlorvk, UserLastName: Ljhbidsw, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:21 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:23 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fnvlorvk","userLastName":"Ljhbidsw","username":"fljhbidsw1481","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_mnpjlayiky","practiceUsername":"aq37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:23 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:23 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:28 PM</td>
        <td>
          Generated practiceUsername is: tn37891 and vendorUsername: nnewvendor3879 and vendorPassword: w4xcd3ro
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:29 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831039 and practiceId: 22320069162 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:29 PM</td>
        <td>
          LocationId: 22113852575
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:30 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:31 PM</td>
        <td>
          Username: fletjwjks1451, Password: i4g9tbmg (encrypted: k7m/oALBA9Qi1WIVvmPIvQ==), SystemName: auto_qa_kguuoneqzc, UserFirstName: Fzfldtsd, UserLastName: Letjwjks, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:31 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:33 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fzfldtsd","userLastName":"Letjwjks","username":"fletjwjks1451","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_kguuoneqzc","practiceUsername":"tn37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:33 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:33 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:39 PM</td>
        <td>
          Generated practiceUsername is: km37892 and vendorUsername: nnewvendor2624 and vendorPassword: otbencmv
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:40 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831040 and practiceId: 22320069192 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:40 PM</td>
        <td>
          LocationId: 22113852576
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:41 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:41 PM</td>
        <td>
          Username: flgvespnk1464, Password: 5wy9u1cd (encrypted: 8AgPqFo7LSknNh6h00hyxA==), SystemName: auto_qa_whfbuwazcw, UserFirstName: Fhgzcyqu, UserLastName: Lgvespnk, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:42 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:45 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fhgzcyqu","userLastName":"Lgvespnk","username":"flgvespnk1464","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_whfbuwazcw","practiceUsername":"km37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:45 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:45 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:50 PM</td>
        <td>
          Generated practiceUsername is: zv37891 and vendorUsername: nnewvendor5289 and vendorPassword: fv9ozf0f
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:50 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831041 and practiceId: 22320069222 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:50 PM</td>
        <td>
          LocationId: 22113852577
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:52 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:52 PM</td>
        <td>
          Username: flsdxrbgp1167, Password: xh49r71b (encrypted: QDr8ZzM77bR6K85JcNlrYw==), SystemName: auto_qa_iuelqtoodx, UserFirstName: Fxzwzaej, UserLastName: Lsdxrbgp, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:53 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:55 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fxzwzaej","userLastName":"Lsdxrbgp","username":"flsdxrbgp1167","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_iuelqtoodx","practiceUsername":"zv37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:55 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:14:55 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:00 PM</td>
        <td>
          Generated practiceUsername is: bw3789 and vendorUsername: nnewvendor7615 and vendorPassword: 7pfqtyd1
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:01 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831042 and practiceId: 22320069252 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:01 PM</td>
        <td>
          LocationId: 22113852578
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:02 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:02 PM</td>
        <td>
          Username: fllrsrljz1279, Password: ynhudbp9 (encrypted: tUe3gaBWM1FH5A4PKVaMtQ==), SystemName: auto_qa_prarkyuoqq, UserFirstName: Fsukifix, UserLastName: Llrsrljz, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:03 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:05 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fsukifix","userLastName":"Llrsrljz","username":"fllrsrljz1279","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_prarkyuoqq","practiceUsername":"bw3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:05 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:05 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:11 PM</td>
        <td>
          Generated practiceUsername is: uv37892 and vendorUsername: nnewvendor3884 and vendorPassword: 2wbeweoe
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:11 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831043 and practiceId: 22320069282 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:11 PM</td>
        <td>
          LocationId: 22113852579
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:13 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:13 PM</td>
        <td>
          Username: flnnucpxf1086, Password: vpp2nhb6 (encrypted: /63gtK3A+8w+ly2RDR2b+A==), SystemName: auto_qa_nyhwhxzamv, UserFirstName: Fbgfcvnn, UserLastName: Lnnucpxf, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:13 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:16 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fbgfcvnn","userLastName":"Lnnucpxf","username":"flnnucpxf1086","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_nyhwhxzamv","practiceUsername":"uv37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:16 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:16 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:21 PM</td>
        <td>
          Generated practiceUsername is: sm37892 and vendorUsername: nnewvendor9848 and vendorPassword: jdnoyb8a
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:22 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831044 and practiceId: 22320069312 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:22 PM</td>
        <td>
          LocationId: 22113852580
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:23 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:23 PM</td>
        <td>
          Username: fluryejkw1468, Password: qq1wcv6w (encrypted: j6ZDbKJOoan2grGSH0KgQg==), SystemName: auto_qa_vsaoobwfoz, UserFirstName: Flujqwix, UserLastName: Luryejkw, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:24 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:26 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Flujqwix","userLastName":"Luryejkw","username":"fluryejkw1468","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_vsaoobwfoz","practiceUsername":"sm37892","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:26 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:26 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:30 PM</td>
        <td>
          Generated practiceUsername is: aa3789 and vendorUsername: nnewvendor1244 and vendorPassword: rg00hg56
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:32 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831045 and practiceId: 22320069342 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:32 PM</td>
        <td>
          LocationId: 22113852581
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:33 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:33 PM</td>
        <td>
          Username: flfmjerrv1424, Password: q97ykl02 (encrypted: mRtzeQ5jNZOA4VFIBi1F+A==), SystemName: auto_qa_vcdkpndqpk, UserFirstName: Fmtrfqsc, UserLastName: Lfmjerrv, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:34 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:36 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fmtrfqsc","userLastName":"Lfmjerrv","username":"flfmjerrv1424","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_vcdkpndqpk","practiceUsername":"aa3789","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:37 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:37 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:45 PM</td>
        <td>
          Generated practiceUsername is: xp37894 and vendorUsername: nnewvendor8592 and vendorPassword: 91rpzjwx
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:46 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831046 and practiceId: 22320069372 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:46 PM</td>
        <td>
          LocationId: 22113852582
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:47 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:47 PM</td>
        <td>
          Username: fljhucttf1728, Password: c62vmr0j (encrypted: 0PWzE3fdOpHbzSh1P7VYiQ==), SystemName: auto_qa_mpnwuuowpy, UserFirstName: Fbmuvfsa, UserLastName: Ljhucttf, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:48 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:50 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fbmuvfsa","userLastName":"Ljhucttf","username":"fljhucttf1728","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_mpnwuuowpy","practiceUsername":"xp37894","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:50 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:50 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:58 PM</td>
        <td>
          Generated practiceUsername is: mh37891 and vendorUsername: nnewvendor9320 and vendorPassword: skjjcap8
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:59 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831047 and practiceId: 22320069402 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:15:59 PM</td>
        <td>
          LocationId: 22113852583
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:00 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:00 PM</td>
        <td>
          Username: fltrrfket1934, Password: kpe4sm44 (encrypted: L0QfCG4Fj74gTpqoUP/THw==), SystemName: auto_qa_ivnizsfpbk, UserFirstName: Fdghfncg, UserLastName: Ltrrfket, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:01 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:03 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fdghfncg","userLastName":"Ltrrfket","username":"fltrrfket1934","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_ivnizsfpbk","practiceUsername":"mh37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:03 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:03 PM</td>
        <td>
          Test data loaded.
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:07 PM</td>
        <td>
          Generated practiceUsername is: lg37891 and vendorUsername: nnewvendor5538 and vendorPassword: amb21e83
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:08 PM</td>
        <td>
          practiceLevelId(organizationId): 22124831048 and practiceId: 22320069432 have been linked by each other
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:08 PM</td>
        <td>
          LocationId: 22113852584
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:09 PM</td>
        <td>
          Traditional SSO has been created successfully
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:09 PM</td>
        <td>
          Username: flvrvgtcn1307, Password: g7lxdebh (encrypted: EI9btPuRR1w6ga50EeJVeQ==), SystemName: auto_qa_vkljonvsuo, UserFirstName: Fwgsqwfr, UserLastName: Lvrvgtcn, UserSuffix: D, extOrgPassword(encrypted): W4+/TEdhxhYqw/BHyTDc5Q==
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:10 PM</td>
        <td>
          Get Token Via WebLogin
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:12 PM</td>
        <td>
          Login json object: {"loginType":"ssoLogin","userFirstName":"Fwgsqwfr","userLastName":"Lvrvgtcn","username":"flvrvgtcn1307","password":"ZO4hRKpJXIZGe71b18+iYg==","systemName":"auto_qa_vkljonvsuo","practiceUsername":"lg37891","extOrgPassword":"W4+\/TEdhxhYqw\/BHyTDc5Q==","screen":"patient"}
        </td>
      </tr>
      <tr class="event-row">
        <td><span class="badge log pass-bg">Pass</span></td>
        <td>12:16:12 PM</td>
        <td>
          com.drfirst.rcopia.automation.test.tools.UserRegistration.test passed
        </td>
      </tr>
  </tbody>
</table>
</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
<div class="test-content scrollable">
<div class="test-content-tools">
<ul><li><a class="back-to-test" href="#"><i class="fa fa-arrow-left"></i></a></li></ul>
</div>
<div class="test-content-detail"><div class="detail-body"></div></div>
</div></div>
<div class="container-fluid p-4 view dashboard-view">
<div class="row">
<div class="col-md-3">
<div class="card"><div class="card-body">
<p class="m-b-0">Started</p>
<h3>Sep 9, 2024 11:56:57 AM</h3>
</div></div>
</div>
<div class="col-md-3">
<div class="card"><div class="card-body">
<p class="m-b-0">Ended</p>
<h3>Sep 9, 2024 12:16:12 PM</h3>
</div></div>
</div>
<div class="col-md-3">
<div class="card"><div class="card-body">
<p class="m-b-0 text-pass">Tests Passed</p>
<h3>1</h3>
</div></div>
</div>
<div class="col-md-3">
<div class="card"><div class="card-body">
<p class="m-b-0 text-fail">Tests Failed</p>
<h3>0</h3>
</div></div>
</div>
</div>
<div class="row">
<div class="col-md-6">
<div class="card">
<div class="card-header">
<h6 class="card-title">Tests</h6>
</div>
<div class="card-body">
<div class="">
<canvas id='parent-analysis' width='115' height='90'></canvas>
</div>
</div>
<div class="card-footer">
<div><small data-tooltip='100%'>
<b>1</b> tests passed
</small>
</div>
<div>
<small data-tooltip='0%'><b>0</b> tests failed,
<b>0</b> skipped, <b data-tooltip='0%'>0</b> others
</small>
</div>
</div>
</div>
</div>
<div class="col-md-6">
<div class="card">
<div class="card-header">
<h6 class="card-title">Log events</h6>
</div>
<div class="card-body">
<div class="">
<canvas id='events-analysis' width='115' height='90'></canvas>
</div>
</div>
<div class="card-footer">
<div><small data-tooltip='100%'><b>900</b> events passed</small></div>
<div>
<small data-tooltip='0%'><b>0</b> events failed,
<b data-tooltip='%'>0</b> others
</small>
</div>
</div>
</div>
</div>
</div>
<div class="row"><div class="col-md-12">
<div class="card"><div class="card-header"><p>Timeline</p></div>
<div class="card-body pt-0"><div>
<canvas id="timeline" height="120"></canvas>
</div></div>
</div>
</div></div>
<script>
var timeline = {
"UserRegistration":1154.538
};
</script>
<div class="row">
<div class="col-lg-6 col-md-12 sysenv-container">
<div class="card">
<div class="card-header"><p>System/Environment</p></div>
<div class="card-body pb-0 pt-0"><table class="table table-sm table-bordered">
<thead><tr class="bg-gray"><th>Name</th><th>Value</th></tr></thead>
<tbody>
<tr>
<td>RPS</td>
<td>placeholder</td>
</tr>
<tr>
<td>GDOCMILLER</td>
<td>placeholder</td>
</tr>
<tr>
<td>GAUTH</td>
<td>placeholder</td>
</tr>
<tr>
<td>ORCA</td>
<td>placeholder</td>
</tr>
<tr>
<td>GAUDITREPORT</td>
<td>placeholder</td>
</tr>
<tr>
<td>GREPO</td>
<td>placeholder</td>
</tr>
</tbody>
</table></div>
</div>
</div>
</div>
</div>
<script>
var statusGroup = {
parentCount: 5,
passParent: 1,
failParent: 0,
warningParent: 0,
skipParent: 0,
childCount: 5,
passChild: 0,
failChild: 0,
warningChild: 0,
skipChild: 0,
infoChild: 0,
grandChildCount: 5,
passGrandChild: 0,
failGrandChild: 0,
warningGrandChild: 0,
skipGrandChild: 0,
infoGrandChild: 0,
eventsCount: 5,
passEvents: 900,
failEvents: 0,
warningEvents: 0,
skipEvents: 0,
infoEvents: 0
};
</script>        </div>
      </div>
    </div>
  </div>
<script src="https://cdn.jsdelivr.net/gh/extent-framework/extent-github-cdn@d6562a79075e061305ccfdb82f01e5e195e2d307/spark/js/spark-script.js"></script>
<script type="text/javascript"></script></body>
</html>
'''

# Regular expression to find usernames
username_pattern = r'Username: (\w+),'

# Extract usernames
usernames = re.findall(username_pattern, html_content)

# Create a directory to store the JSON files
if not os.path.exists('usernames'):
    os.makedirs('usernames')

# Create individual JSON files for each username
for username in usernames:
    user_data = {
        "username": username,
        "password": "Test1234"
    }
    
    filename = f'usernames/{username}.json'
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=2)
    
    print(f"Created {filename}")

# Create a single JSON file with all usernames
all_users_data = [{"username": username, "password": "Test1234"} for username in usernames]

with open('usernames/all_usernames.json', 'w') as f:
    json.dump(all_users_data, f, indent=2)

print("Created usernames/all_usernames.json")

print(f"Total usernames processed: {len(usernames)}")
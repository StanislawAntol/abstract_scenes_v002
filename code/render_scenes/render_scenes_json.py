


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    
    
    <title>abstract_scenes_v002/render_scenes_json.py at vqa-master · StanislawAntol/abstract_scenes_v002 · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="StanislawAntol/abstract_scenes_v002" name="twitter:title" /><meta content="abstract_scenes_v002 - The second version of the interface for Abstract Scenes research project." name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/1846231?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/1846231?v=3&amp;s=400" property="og:image" /><meta content="StanislawAntol/abstract_scenes_v002" property="og:title" /><meta content="https://github.com/StanislawAntol/abstract_scenes_v002" property="og:url" /><meta content="abstract_scenes_v002 - The second version of the interface for Abstract Scenes research project." property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
        <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="80AD58FC:108E:ED64C38:560AF1C8" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged Out">
      <meta class="js-ga-set" name="dimension4" content="Current repo nav">
    <meta name="is-dotcom" content="true">
        <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

      <!-- </textarea> --><!-- '"` --><meta content="authenticity_token" name="csrf-param" />
<meta content="BJFY4TiQcsFZtu7NsuxMLt+OLWsxAFoEHi3dwu9jC9w/pZ5RuvozVtVf+uNZ/nOCikxgrsvizUN4caNPCLqoWg==" name="csrf-token" />
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-52cc21dbf169e4dc2f833078b8f50f822cd69777c8489192f261ee8a5dea311f.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2-b0c508ae0fcef1b58088ceb97448056a48c03818895f2e43ef5ffe6d21652738.css" media="all" rel="stylesheet" />
    
    
    


    <meta http-equiv="x-pjax-version" content="b512a011da40169c18ea4e5545788172">

      
  <meta name="description" content="abstract_scenes_v002 - The second version of the interface for Abstract Scenes research project.">
  <meta name="go-import" content="github.com/StanislawAntol/abstract_scenes_v002 git https://github.com/StanislawAntol/abstract_scenes_v002.git">

  <meta content="1846231" name="octolytics-dimension-user_id" /><meta content="StanislawAntol" name="octolytics-dimension-user_login" /><meta content="31018613" name="octolytics-dimension-repository_id" /><meta content="StanislawAntol/abstract_scenes_v002" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="31018613" name="octolytics-dimension-repository_network_root_id" /><meta content="StanislawAntol/abstract_scenes_v002" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/StanislawAntol/abstract_scenes_v002/commits/vqa-master.atom" rel="alternate" title="Recent Commits to abstract_scenes_v002:vqa-master" type="application/atom+xml">

  </head>


  <body class="logged_out   env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



      
      
      <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="btn btn-primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="btn" href="/login?return_to=%2FStanislawAntol%2Fabstract_scenes_v002%2Fblob%2Fvqa-master%2Fcode%2Frender_scenes%2Frender_scenes_json.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/StanislawAntol/abstract_scenes_v002/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/StanislawAntol/abstract_scenes_v002/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/pricing" data-ga-click="(Logged out) Header, go to pricing, text:pricing">Pricing</a>
          </li>
      </ul>

  </div>
</div>



    <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/WebPage">
    <div class="pagehead repohead instapaper_ignore readability-menu">

      <div class="container">

        <div class="clearfix">
          
<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2FStanislawAntol%2Fabstract_scenes_v002"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <span class="octicon octicon-eye"></span>
    Watch
  </a>
  <a class="social-count" href="/StanislawAntol/abstract_scenes_v002/watchers">
    1
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2FStanislawAntol%2Fabstract_scenes_v002"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/StanislawAntol/abstract_scenes_v002/stargazers">
      1
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2FStanislawAntol%2Fabstract_scenes_v002"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>

    <a href="/StanislawAntol/abstract_scenes_v002/network" class="social-count">
      2
    </a>
  </li>
</ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public ">
  <span class="mega-octicon octicon-repo"></span>
  <span class="author"><a href="/StanislawAntol" class="url fn" itemprop="url" rel="author"><span itemprop="title">StanislawAntol</span></a></span><!--
--><span class="path-divider">/</span><!--
--><strong><a href="/StanislawAntol/abstract_scenes_v002" data-pjax="#js-repo-pjax-container">abstract_scenes_v002</a></strong>

  <span class="page-context-loader">
    <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
  </span>

</h1>

        </div>
      </div>
    </div>

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline ">
        <div class="repository-sidebar clearfix">
          
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/StanislawAntol/abstract_scenes_v002/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/StanislawAntol/abstract_scenes_v002/tree/vqa-master" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /StanislawAntol/abstract_scenes_v002/tree/vqa-master">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/StanislawAntol/abstract_scenes_v002/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /StanislawAntol/abstract_scenes_v002/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/StanislawAntol/abstract_scenes_v002/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /StanislawAntol/abstract_scenes_v002/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/StanislawAntol/abstract_scenes_v002/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /StanislawAntol/abstract_scenes_v002/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/StanislawAntol/abstract_scenes_v002/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /StanislawAntol/abstract_scenes_v002/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

            <div class="only-with-full-nav">
                
<div class="js-clone-url clone-url open"
  data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/StanislawAntol/abstract_scenes_v002.git" readonly="readonly" aria-label="HTTPS clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/StanislawAntol/abstract_scenes_v002" readonly="readonly" aria-label="Subversion checkout URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<div class="clone-options">You can clone with
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone" class="inline-form js-clone-selector-form " data-form-nonce="8b6fabeaa3458b4a27da6120e27bde2b89dc54be" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="1RbLj8yGYVbGALBfQEkQDaApUG8AlStFHceiNk8cl1wQUJe4rgiQ1jlDYa9qNhoA+1vdIgKBEM+lKuxHhuh4Cg==" /></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form> or <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone" class="inline-form js-clone-selector-form " data-form-nonce="8b6fabeaa3458b4a27da6120e27bde2b89dc54be" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="544ijXESswVrkfVIJ5NjgrPbChws7Xl6/5CtFHQ5BgCIRU5DsEX1aaB7QW8dhnU3qem4yoise2EPz7QwT9n9Hg==" /></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</div>

              <a href="/StanislawAntol/abstract_scenes_v002/archive/vqa-master.zip"
                 class="btn btn-sm sidebar-button"
                 aria-label="Download the contents of StanislawAntol/abstract_scenes_v002 as a zip file"
                 title="Download the contents of StanislawAntol/abstract_scenes_v002 as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div>
        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/StanislawAntol/abstract_scenes_v002/blob/214dac7e3185feb73844d61f60201b5f062f5c3f/code/render_scenes/render_scenes_json.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:88357f1584acc6ff22b49a2f99b8dae9 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-ref="vqa-master"
    title="vqa-master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">vqa-master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/StanislawAntol/abstract_scenes_v002/blob/before_paperdoll/code/render_scenes/render_scenes_json.py"
               data-name="before_paperdoll"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="before_paperdoll">
                before_paperdoll
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/StanislawAntol/abstract_scenes_v002/blob/master/code/render_scenes/render_scenes_json.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/StanislawAntol/abstract_scenes_v002/blob/vqa-master/code/render_scenes/render_scenes_json.py"
               data-name="vqa-master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="vqa-master">
                vqa-master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="btn-group right">
      <a href="/StanislawAntol/abstract_scenes_v002/find/vqa-master"
            class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-nw"
            data-pjax
            data-hotkey="t"
            aria-label="Quickly jump between files">
        <span class="octicon octicon-list-unordered"></span>
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </div>

    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/StanislawAntol/abstract_scenes_v002/tree/vqa-master" class="" data-branch="vqa-master" data-pjax="true" itemscope="url"><span itemprop="title">abstract_scenes_v002</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/StanislawAntol/abstract_scenes_v002/tree/vqa-master/code" class="" data-branch="vqa-master" data-pjax="true" itemscope="url"><span itemprop="title">code</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/StanislawAntol/abstract_scenes_v002/tree/vqa-master/code/render_scenes" class="" data-branch="vqa-master" data-pjax="true" itemscope="url"><span itemprop="title">render_scenes</span></a></span><span class="separator">/</span><strong class="final-path">render_scenes_json.py</strong>
    </div>
  </div>

<include-fragment class="commit commit-loader file-history-tease" src="/StanislawAntol/abstract_scenes_v002/contributors/vqa-master/code/render_scenes/render_scenes_json.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/StanislawAntol/abstract_scenes_v002/raw/vqa-master/code/render_scenes/render_scenes_json.py" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/StanislawAntol/abstract_scenes_v002/blame/vqa-master/code/render_scenes/render_scenes_json.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/StanislawAntol/abstract_scenes_v002/commits/vqa-master/code/render_scenes/render_scenes_json.py" class="btn btn-sm " rel="nofollow">History</a>
    </div>


        <button type="button" class="octicon-btn disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-pencil"></span>
        </button>
        <button type="button" class="octicon-btn octicon-btn-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </button>
  </div>

  <div class="file-info">
      434 lines (344 sloc)
      <span class="file-info-divider"></span>
    17.1 KB
  </div>
</div>

  

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"> <span class="pl-c">#!/usr/bin/python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"> <span class="pl-c"># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> PIL <span class="pl-k">import</span> Image, ImageFilter</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> os <span class="pl-k">import</span> path</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> glob</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> math</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> numpy <span class="pl-k">import</span> matrix</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> numpy <span class="pl-k">import</span> linalg</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pdb</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">dir_path</span>(<span class="pl-smi">dname</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    If the directory doesn&#39;t exist then make it.</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">        os.makedirs(dname)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> os.error:</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> dname</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">RenderScenes</span>(<span class="pl-e"><span class="pl-c1">object</span></span>):</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">opts</span>):</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.opts <span class="pl-k">=</span> opts</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.prev_scene_config_file <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">run</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>render<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.render_scenes()</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">render_scenes</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#&quot;pilot_01.json&quot;</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        json_data <span class="pl-k">=</span> <span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;jsondata&gt;<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#render_dir = &#39;../imgs/&#39;</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        render_dir <span class="pl-k">=</span> dir_path(<span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;outdir&gt;<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        clipart_img_format <span class="pl-k">=</span> <span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--format<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.overwrite <span class="pl-k">=</span> <span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--overwrite<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--site_pngs_dir<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>USE_DEF<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#base_url_interface = os.path.join(&#39;..&#39;, &#39;..&#39;, &#39;interface&#39;)</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            base_url_interface <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/srv/share/abstract_scenes_v002/site_pngs/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            base_url_interface <span class="pl-k">=</span> <span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--site_pngs_dir<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--config_dir<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>USE_DEF<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#config_folder = dir_path(os.path.join(&#39;..&#39;, &#39;..&#39;, &#39;data&#39;))</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">            config_folder <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/srv/share/abstract_scenes_v002/site_data/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">            config_folder <span class="pl-k">=</span> <span class="pl-v">self</span>.opts[<span class="pl-s"><span class="pl-pds">&#39;</span>--config_dir<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.config_folder <span class="pl-k">=</span> config_folder</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.render_dir <span class="pl-k">=</span> render_dir</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.clipart_img_format <span class="pl-k">=</span> clipart_img_format</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.base_url_interface <span class="pl-k">=</span> base_url_interface</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> path.isdir(json_data):</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            search_str <span class="pl-k">=</span> path.join(json_data, <span class="pl-s"><span class="pl-pds">&#39;</span>*.json<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">            json_files <span class="pl-k">=</span> glob.glob(search_str)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">            json_files.sort()</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> json_file <span class="pl-k">in</span> json_files:</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">with</span> <span class="pl-c1">open</span>(json_file) <span class="pl-k">as</span> json_fileid:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">                    scene <span class="pl-k">=</span> json.load(json_fileid)    </td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.render_one_scene(scene)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(json_data) <span class="pl-k">as</span> json_fileid:</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">                all_scenes <span class="pl-k">=</span> json.load(json_fileid)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">type</span>(all_scenes) <span class="pl-k">==</span> <span class="pl-c1">list</span>:</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> cur_scene <span class="pl-k">in</span> all_scenes:</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.render_one_scene(cur_scene)</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">type</span>(all_scenes) <span class="pl-k">==</span> <span class="pl-c1">dict</span>:</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.render_one_scene(all_scenes)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">render_one_scene</span>(<span class="pl-smi">self</span>, <span class="pl-smi">data</span>):</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>imgName<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> data:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            img_name <span class="pl-k">=</span> data[<span class="pl-s"><span class="pl-pds">&#39;</span>imgName<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>file_name<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> data:</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">            img_name <span class="pl-k">=</span> data[<span class="pl-s"><span class="pl-pds">&#39;</span>file_name<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> data:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            img_name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>.png<span class="pl-pds">&#39;</span></span>.format(data[<span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        img_file <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.render_dir, img_name)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Skip if already exists and no overwrite flag</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (<span class="pl-k">not</span> os.path.isfile(img_file) <span class="pl-k">or</span> <span class="pl-v">self</span>.overwrite<span class="pl-k">==</span><span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">            cur_scene <span class="pl-k">=</span> data[<span class="pl-s"><span class="pl-pds">&#39;</span>scene<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.read_scene_config_file(cur_scene[<span class="pl-s"><span class="pl-pds">&#39;</span>sceneConfigFile<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">            cur_scene_type <span class="pl-k">=</span> cur_scene[<span class="pl-s"><span class="pl-pds">&#39;</span>sceneType<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">            cur_scene_config <span class="pl-k">=</span> <span class="pl-v">self</span>.scene_config_data[cur_scene_type]</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">            def_z_size <span class="pl-k">=</span>  cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>defZSize<span class="pl-pds">&#39;</span></span>]   </td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">            img_pad_num <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>imgPadNum<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">            not_used <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>notUsed<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">            num_z_size <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>numZSize<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">            num_depth0 <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>numDepth0<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">            num_depth1 <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>numDepth1<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">            num_flip <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>numFlip<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">            object_type_data <span class="pl-k">=</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>objectTypeData<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">            object_type_order <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">            num_obj_type_show <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> obj_el <span class="pl-k">in</span> object_type_data:</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">                cur_name <span class="pl-k">=</span> obj_el[<span class="pl-s"><span class="pl-pds">&#39;</span>nameType<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">                object_type_order.append(cur_name)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">                num_obj_type_show[cur_name] <span class="pl-k">=</span> obj_el[<span class="pl-s"><span class="pl-pds">&#39;</span>numShow<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">            cur_avail_obj <span class="pl-k">=</span> cur_scene[<span class="pl-s"><span class="pl-pds">&#39;</span>availableObject<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">            cur_z_scale <span class="pl-k">=</span> [<span class="pl-c1">1.0</span>]</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>, num_z_size):</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">                cur_z_scale.append(cur_z_scale[i <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">*</span> cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>zSizeDecay<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">            bg_img_file <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, </td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">                                cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>baseDir<span class="pl-pds">&#39;</span></span>], </td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">                                cur_scene_config[<span class="pl-s"><span class="pl-pds">&#39;</span>bgImg<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            bg_img <span class="pl-k">=</span> Image.open(bg_img_file)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># // Make sure we get the depth ordering correct (render the objects using their depth order)</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">reversed</span>(<span class="pl-c1">range</span>(<span class="pl-c1">0</span>, num_depth0)): <span class="pl-c"># (num_depth0-1, num_depth0-2, ... 0)</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#     if (curDepth0Used[k] &lt;= 0) { // not used, just to accelerate the process</span></td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#         continue;</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#     }</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> j <span class="pl-k">in</span> <span class="pl-c1">reversed</span>(<span class="pl-c1">range</span>(<span class="pl-c1">0</span>, num_z_size<span class="pl-k">+</span><span class="pl-c1">1</span>)):</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#         // for people, choose both the expression and the pose</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> L <span class="pl-k">in</span> <span class="pl-c1">reversed</span>(<span class="pl-c1">range</span>(<span class="pl-c1">0</span>, num_depth1)):</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#             if (curDepth1Used[l] &lt;= 0) { // not used, just to accelerate the process</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#                 continue;</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#             }</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>, <span class="pl-c1">len</span>(cur_avail_obj)):</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">if</span> (cur_avail_obj[i][<span class="pl-s"><span class="pl-pds">&#39;</span>instance<span class="pl-pds">&#39;</span></span>][<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>depth0<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> k):</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                                <span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>, cur_avail_obj[i][<span class="pl-s"><span class="pl-pds">&#39;</span>numInstance<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">                                    cur_obj <span class="pl-k">=</span> cur_avail_obj[i][<span class="pl-s"><span class="pl-pds">&#39;</span>instance<span class="pl-pds">&#39;</span></span>][m]</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-k">if</span> (cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>present<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">True</span> <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">                                        cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>z<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> j <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">                                        cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>depth1<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> L):</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                                        </td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                                        <span class="pl-k">if</span> (cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">                                            <span class="pl-k">if</span> (cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                                                <span class="pl-v">self</span>.overlay_deformable_person(bg_img, img_pad_num,</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">                                                                               cur_obj, cur_z_scale)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                                            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                                                <span class="pl-v">self</span>.overlay_nondeformable_person(bg_img, img_pad_num,</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">                                                                                  cur_obj, cur_z_scale)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">                                        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">                                            <span class="pl-v">self</span>.overlay_nondeformable_obj(bg_img, img_pad_num,</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                                                                           cur_obj, cur_z_scale)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">            bg_img.save(img_file, <span class="pl-v">self</span>.clipart_img_format, <span class="pl-smi">compress_level</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">optimize</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">read_scene_config_file</span>(<span class="pl-smi">self</span>, <span class="pl-smi">scene_config_filename</span>):</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        scene_config_file <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.config_folder, scene_config_filename)</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Only need to load if not the same as previous</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (scene_config_file <span class="pl-k">!=</span> <span class="pl-v">self</span>.prev_scene_config_file):</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.prev_scene_config_file <span class="pl-k">=</span> scene_config_file</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(scene_config_file) <span class="pl-k">as</span> json_fileid:</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.scene_config_data <span class="pl-k">=</span> json.load(json_fileid)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">                obj_filenames <span class="pl-k">=</span> <span class="pl-v">self</span>.scene_config_data[<span class="pl-s"><span class="pl-pds">&#39;</span>clipartObjJSONFile<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">                object_data <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> obj_file <span class="pl-k">in</span> obj_filenames:</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">                    obj_file_vers <span class="pl-k">=</span> obj_file[<span class="pl-s"><span class="pl-pds">&#39;</span>file<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> obj_dtype, obj_type_file <span class="pl-k">in</span> obj_file_vers.items():</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">with</span> <span class="pl-c1">open</span>(os.path.join(<span class="pl-v">self</span>.config_folder, obj_type_file)) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">                            obj <span class="pl-k">=</span> json.load(f)</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">if</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>objectType<span class="pl-pds">&#39;</span></span>] <span class="pl-k">not</span> <span class="pl-k">in</span> object_data:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">                                object_data[obj[<span class="pl-s"><span class="pl-pds">&#39;</span>objectType<span class="pl-pds">&#39;</span></span>]] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">                            object_data[obj[<span class="pl-s"><span class="pl-pds">&#39;</span>objectType<span class="pl-pds">&#39;</span></span>]][obj_dtype] <span class="pl-k">=</span> obj</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.object_data <span class="pl-k">=</span> object_data</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_object_attr_types</span>(<span class="pl-smi">self</span>, <span class="pl-smi">obj_type</span>, <span class="pl-smi">deform_type</span>):</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">        cur_attr_types <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> cur_attr_name <span class="pl-k">in</span> <span class="pl-v">self</span>.object_data[obj_type][deform_type][<span class="pl-s"><span class="pl-pds">&#39;</span>attributeTypeList<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">            cur_attr_type <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (cur_attr_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Type<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">                cur_attr_type <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>num<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>numType<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>typeID<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> (cur_attr_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Pose<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">                cur_attr_type <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>num<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>numPose<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>poseID<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> (cur_attr_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Expression<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">                cur_attr_type <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>num<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>numExpression<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>expressionID<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">            cur_attr_types.append(cur_attr_type)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> cur_attr_types</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">obj_img_filename</span>(<span class="pl-smi">self</span>, <span class="pl-smi">img_pad_num</span>, <span class="pl-smi">obj</span>, <span class="pl-smi">attr1</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">attr2</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">attr3</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">        object_data <span class="pl-k">=</span> <span class="pl-v">self</span>.object_data</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># TODO Don&#39;t hardcode this?</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">        clipart_img_format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>png<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">        cur_obj_type <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">        cur_obj_name <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">            cur_obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">            cur_obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>nondeformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        cur_attr_types <span class="pl-k">=</span> <span class="pl-v">self</span>.get_object_attr_types(cur_obj_type, cur_obj_deform)</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (attr1 <span class="pl-k">==</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            attr1 <span class="pl-k">=</span> obj[cur_attr_types[<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>largeObject<span class="pl-pds">&#39;</span></span> <span class="pl-k">or</span> cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>smallObject<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">            sceneFolder <span class="pl-k">=</span> <span class="pl-v">self</span>.scene_config_data[<span class="pl-s"><span class="pl-pds">&#39;</span>baseDirectory<span class="pl-pds">&#39;</span></span>][obj[<span class="pl-s"><span class="pl-pds">&#39;</span>baseDir<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}{1}</span>.<span class="pl-c1">{2}</span><span class="pl-pds">&#39;</span></span>.format(cur_obj_name,</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-c1">str</span>(attr1<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num), </td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                                    clipart_img_format)</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, sceneFolder, name)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> (cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>animal<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">            animalFolder <span class="pl-k">=</span> object_data[<span class="pl-s"><span class="pl-pds">&#39;</span>animal<span class="pl-pds">&#39;</span></span>][cur_obj_deform][<span class="pl-s"><span class="pl-pds">&#39;</span>baseDirectory<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}{1}</span>.<span class="pl-c1">{2}</span><span class="pl-pds">&#39;</span></span>.format(cur_obj_name,</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-c1">str</span>(attr1<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num), </td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">                                    clipart_img_format)</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, animalFolder, name)       </td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> (cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (attr2 <span class="pl-k">==</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">                attr2 <span class="pl-k">=</span> obj[cur_attr_types[<span class="pl-c1">1</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (attr3 <span class="pl-k">==</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                attr3 <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>styleID<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">            humanFolder <span class="pl-k">=</span> object_data[<span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>][cur_obj_deform][<span class="pl-s"><span class="pl-pds">&#39;</span>baseDirectory<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">            styleFolder <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}{1}</span><span class="pl-pds">&#39;</span></span>.format(cur_obj_name, </td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                                        <span class="pl-c1">str</span>(attr3<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num))</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}{1}</span>.<span class="pl-c1">{2}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">str</span>(attr2<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num), </td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-c1">str</span>(attr1<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num), </td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">                                    clipart_img_format)</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, humanFolder, styleFolder, name)</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> filename</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">## Needed for the interface but not here (loads just the heads w/ expr)</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">## TODO Update to support this class</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">obj_expr_filename</span>(<span class="pl-smi">self</span>, <span class="pl-smi">img_pad_num</span>, <span class="pl-smi">obj</span>):</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">        filename <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">        clipart_img_format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>png<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">        cur_obj_type <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">        cur_obj_name <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">            obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">            obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>nondeformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            humanFolder <span class="pl-k">=</span> <span class="pl-v">self</span>.object_data[<span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>][obj_deform][<span class="pl-s"><span class="pl-pds">&#39;</span>baseDirectory<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}{1}</span>.<span class="pl-c1">{2}</span><span class="pl-pds">&#39;</span></span>.format(cur_obj_name, </td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                                       <span class="pl-c1">str</span>(obj[<span class="pl-s"><span class="pl-pds">&#39;</span>expressionID<span class="pl-pds">&#39;</span></span>]<span class="pl-k">+</span><span class="pl-c1">1</span>).zfill(img_pad_num),</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                                        clipart_img_format)</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, humanFolder, </td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-s"><span class="pl-pds">&#39;</span>Expressions<span class="pl-pds">&#39;</span></span>, name)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> filename</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">paperdoll_part_img_filename_expr</span>(<span class="pl-smi">self</span>, <span class="pl-smi">obj</span>, <span class="pl-smi">part_name</span>):</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">        filename <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">        cur_obj_type <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">        cur_obj_name <span class="pl-k">=</span> obj[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">            obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>deformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">            obj_deform <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>nondeformable<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        clipart_img_format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>png<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (cur_obj_type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">            humanFolder <span class="pl-k">=</span> <span class="pl-v">self</span>.object_data[<span class="pl-s"><span class="pl-pds">&#39;</span>human<span class="pl-pds">&#39;</span></span>][obj_deform][<span class="pl-s"><span class="pl-pds">&#39;</span>baseDirectory<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}</span>.<span class="pl-c1">{1}</span><span class="pl-pds">&#39;</span></span>.format(part_name, clipart_img_format)</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.base_url_interface, humanFolder, cur_obj_name, name)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> filename</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_render_transform</span>(<span class="pl-smi">self</span>, <span class="pl-smi">X1</span>, <span class="pl-smi">X</span>, <span class="pl-smi">rad</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">scale</span>):</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (flip <span class="pl-k">==</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">            S  <span class="pl-k">=</span> matrix([[scale, <span class="pl-c1">0</span>, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, scale, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">            T1 <span class="pl-k">=</span> matrix([[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>, X1[<span class="pl-c1">0</span>]],</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, X1[<span class="pl-c1">1</span>]],</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">            T2 <span class="pl-k">=</span> matrix([[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>, X[<span class="pl-c1">0</span>]], </td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, X[<span class="pl-c1">1</span>]], </td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">            R  <span class="pl-k">=</span> matrix([[math.cos(rad), <span class="pl-k">-</span>math.sin(rad), <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">                        [math.sin(rad), math.cos(rad), <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">            T <span class="pl-k">=</span> S<span class="pl-k">*</span>T2<span class="pl-k">*</span>R<span class="pl-k">*</span>T1</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: <span class="pl-c"># (flip == 1)</span></td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">            rad <span class="pl-k">*=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">            S  <span class="pl-k">=</span> matrix([[scale, <span class="pl-c1">0</span>, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, scale, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">            T1 <span class="pl-k">=</span> matrix([[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>, X1[<span class="pl-c1">0</span>]],</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, X1[<span class="pl-c1">1</span>]],</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">            T2 <span class="pl-k">=</span> matrix([[<span class="pl-c1">1</span>, <span class="pl-c1">0</span>, <span class="pl-k">-</span>X[<span class="pl-c1">0</span>]], </td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, X[<span class="pl-c1">1</span>]], </td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">            R  <span class="pl-k">=</span> matrix([[math.cos(rad), <span class="pl-k">-</span>math.sin(rad), <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                        [math.sin(rad), math.cos(rad), <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">            F <span class="pl-k">=</span> matrix([[<span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">0</span>, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">1</span>, <span class="pl-c1">0</span>], </td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">                        [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">            T <span class="pl-k">=</span> F<span class="pl-k">*</span>S<span class="pl-k">*</span>T2<span class="pl-k">*</span>R<span class="pl-k">*</span>T1</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">        Tinv <span class="pl-k">=</span> linalg.inv(T);</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">        Tinvtuple <span class="pl-k">=</span> (Tinv[<span class="pl-c1">0</span>,<span class="pl-c1">0</span>], Tinv[<span class="pl-c1">0</span>,<span class="pl-c1">1</span>], Tinv[<span class="pl-c1">0</span>,<span class="pl-c1">2</span>], </td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">                    Tinv[<span class="pl-c1">1</span>,<span class="pl-c1">0</span>], Tinv[<span class="pl-c1">1</span>,<span class="pl-c1">1</span>], Tinv[<span class="pl-c1">1</span>,<span class="pl-c1">2</span>])</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> Tinvtuple</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">overlay_deformable_person</span>(<span class="pl-smi">self</span>, <span class="pl-smi">bg_img</span>, <span class="pl-smi">img_pad_num</span>, <span class="pl-smi">cur_obj</span>, <span class="pl-smi">z_scale</span>):</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">        num_parts <span class="pl-k">=</span> <span class="pl-c1">len</span>(cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>body<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        scale <span class="pl-k">=</span> cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>globalScale<span class="pl-pds">&#39;</span></span>] <span class="pl-k">*</span> z_scale[cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>z<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">        bg_size<span class="pl-k">=</span> bg_img.size</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">        flip <span class="pl-k">=</span> cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>flip<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> partIdx <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span>, num_parts):</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">            part <span class="pl-k">=</span> cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>body<span class="pl-pds">&#39;</span></span>][partIdx]</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">            part_name <span class="pl-k">=</span> part[<span class="pl-s"><span class="pl-pds">&#39;</span>part<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">            X1 <span class="pl-k">=</span> [<span class="pl-k">-</span>part[<span class="pl-s"><span class="pl-pds">&#39;</span>childX<span class="pl-pds">&#39;</span></span>], </td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">                  <span class="pl-k">-</span>part[<span class="pl-s"><span class="pl-pds">&#39;</span>childY<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">            X <span class="pl-k">=</span> [cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformableX<span class="pl-pds">&#39;</span></span>][partIdx], </td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">                 cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformableY<span class="pl-pds">&#39;</span></span>][partIdx]]</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">            rotation <span class="pl-k">=</span> cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>deformableGlobalRot<span class="pl-pds">&#39;</span></span>][partIdx]</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">            Tinvtuple <span class="pl-k">=</span> <span class="pl-v">self</span>.get_render_transform(X1, X, </td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">                                                  rotation, flip, scale)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (part_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Head<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">                part_fn <span class="pl-k">=</span> <span class="pl-v">self</span>.obj_expr_filename(img_pad_num, cur_obj)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">                part_fn <span class="pl-k">=</span> <span class="pl-v">self</span>.paperdoll_part_img_filename_expr(cur_obj, part_name)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># TODO Update so don&#39;t keep opening files for efficiency</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">            part_img <span class="pl-k">=</span> Image.open(part_fn)</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">            part_tf <span class="pl-k">=</span> part_img.transform(bg_size, Image.AFFINE,</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">                                         Tinvtuple, <span class="pl-smi">resample</span><span class="pl-k">=</span>Image.BICUBIC)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            bg_img.paste(part_tf, (<span class="pl-c1">0</span>, <span class="pl-c1">0</span>), part_tf)</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">overlay_nondeformable_person</span>(<span class="pl-smi">self</span>, <span class="pl-smi">bg_img</span>, <span class="pl-smi">img_pad_num</span>, <span class="pl-smi">cur_obj</span>, <span class="pl-smi">z_scale</span>):</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># In our case, we&#39;re just computing the filename and loading it, so </span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># a nondeformable person is the same as nondeformable objects.</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.overlay_nondeformable_obj(bg_img, img_pad_num, cur_obj, z_scale)</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">overlay_nondeformable_obj</span>(<span class="pl-smi">self</span>, <span class="pl-smi">bg_img</span>, <span class="pl-smi">img_pad_num</span>, <span class="pl-smi">cur_obj</span>, <span class="pl-smi">z_scale</span>):</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">        scale <span class="pl-k">=</span> z_scale[cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>z<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># TODO We should just load all possible</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># clipart images once and then index into them </span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># with filename for efficiency</span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        cur_filename <span class="pl-k">=</span> <span class="pl-v">self</span>.obj_img_filename(img_pad_num, cur_obj)</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        cur_clipart_img <span class="pl-k">=</span> Image.open(cur_filename)</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">        (w, h) <span class="pl-k">=</span> cur_clipart_img.size</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">        X <span class="pl-k">=</span> [cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>], cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">        colOffset <span class="pl-k">=</span> <span class="pl-k">-</span>w <span class="pl-k">/</span> <span class="pl-c1">2.0</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">        rowOffset <span class="pl-k">=</span> <span class="pl-k">-</span>h <span class="pl-k">/</span> <span class="pl-c1">2.0</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">        colOffset <span class="pl-k">*=</span> scale</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">        rowOffset <span class="pl-k">*=</span> scale</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">        X[<span class="pl-c1">0</span>] <span class="pl-k">+=</span> colOffset</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">        X[<span class="pl-c1">1</span>] <span class="pl-k">+=</span> rowOffset</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">        offset <span class="pl-k">=</span> (<span class="pl-c1">int</span>(X[<span class="pl-c1">0</span>]), <span class="pl-c1">int</span>(X[<span class="pl-c1">1</span>]))</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">        resized <span class="pl-k">=</span> cur_clipart_img.resize((<span class="pl-c1">int</span>(w<span class="pl-k">*</span>scale), <span class="pl-c1">int</span>(h<span class="pl-k">*</span>scale)), Image.ANTIALIAS)</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (cur_obj[<span class="pl-s"><span class="pl-pds">&#39;</span>flip<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">            bg_img.paste(resized, offset, resized)</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">            flipped <span class="pl-k">=</span> resized.transpose(Image.FLIP_LEFT_RIGHT)</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">            bg_img.paste(flipped, offset, flipped)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Usage:</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        render_scenes_json.py render &lt;jsondata&gt; &lt;outdir&gt; [--overwrite --site_pngs_dir=ID --config_dir=CD --format=FMT]</span></td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                </span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Options:</span></td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        &lt;jsondata&gt;         Either a filepath to JSON file (from other code and extracted from results file) or directory filled with per-scene JSON files.</span></td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        &lt;outdir&gt;            Directory to put the processed result files, i.e., JSON</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        --format=FMT        Image file format [default: png]</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        --site_pngs_dir=ID  Path to the site_pngs dir (contains all object images) [default: USE_DEF]</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        --config_dir=CD     Path to the config data files (contains all object data) [default: USE_DEF]</span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        --overwrite         Overwrite files even if they exist</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#USE_DEF for --site_pngs_dir is /srv/share/abstract_scenes_v002/site_pngs/</span></td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#USE_DEF for --config_dir is /srv/share/abstract_scenes_v002/site_data/</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># 1. set up command line interface</span></td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> docopt, textwrap</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">    main_args <span class="pl-k">=</span> docopt.docopt(textwrap.dedent(main.<span class="pl-c1">__doc__</span>))</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">print</span>(main_args)</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> (main_args[<span class="pl-s"><span class="pl-pds">&#39;</span>render<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">        rend <span class="pl-k">=</span> RenderScenes(main_args)</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">        rend.run()</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">    main()</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>
  </div>


    </div>

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://github.com/pricing" data-ga-click="Footer, go to pricing, text:pricing">Pricing</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.09136s from github-fe139-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <span class="octicon octicon-x"></span>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-f8473dece7242da6a20d52313634881b3975c52cebaa1e6c38157c0f26185691.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-f638d3bf60418b2bc4b943311a0ee3371f41111a06f19ded4b5c4090313d3d7d.js"></script>
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>


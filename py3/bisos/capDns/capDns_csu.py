# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= as equivalent of facter in py and remotely with rpyc.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitist_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitist_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['loadAs'], }
csInfo['version'] = '202606053019'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'gitist_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This a =Cs-Unit= for running the equivalent of facter in py and remotely with rpyc.
With BISOS, it is used in CMDB remotely.

** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import pathlib
import enum
import subprocess
import configparser
from dataclasses import dataclass

import gitlab
import github
from github import Github, Auth

from bisos.gitist import gitist_seedInfo

import logging
log = logging.getLogger(__name__)

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# cs.invOutcomeReportControl(cmnd=True, ro=True)

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    csParams.parDictAdd(
        parName='destBaseDir',
        parDescription="Destination base directory under which repos are cloned (mirroring path_with_namespace).",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        argparseShortOpt=None,
        argparseLongOpt='--destBaseDir',
    )



####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=cli pyInv=pyKwArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             pyKwArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
facterModule.cs -i examples 
  #+end_src
#+RESULTS:
#+begin_example
#+end_example

        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        #  -v 1 --callTrackings monitor+ --callTrackings invoke+
        pars_debug_verbosity = od([('verbosity', "1"),])
        pars_debug_monitor = od([('callTrackings', "monitor+"),])
        pars_debug_invoke = od([('callTrackings', "invoke+"),])
        pars_debug_full = (pars_debug_verbosity | pars_debug_monitor | pars_debug_invoke)

        return(cmndOutcome)


####+BEGIN: b:py3:cs:func/typing :funcName "getGitlab" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /getGitlab/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def getGitlab(
####+END:
) -> gitlab.Gitlab:
    """ #+begin_org
** Build a python-gitlab client from =cmndsControlInfo= (=serverConfigTag=, =serverConfigPath=).
    #+end_org """
    ci = gitist_seedInfo.cmndsControlInfo
    cfgPath = str(pathlib.Path(ci.serverConfigPath).expanduser())
    gl = gitlab.Gitlab.from_config(ci.serverConfigTag, [cfgPath])
    return gl


def _githubCfg():
    """ Read (url, token) from the github cfg INI at serverConfigPath[serverConfigTag].

    When serverConfigTag is unset, fall back to the [global] default tag (like
    python-gitlab's gitlab cfg), then to "default".
    """
    ci = gitist_seedInfo.cmndsControlInfo
    cfgPath = pathlib.Path(ci.serverConfigPath).expanduser()
    parser = configparser.ConfigParser()
    parser.read(str(cfgPath))
    tag = ci.serverConfigTag
    if not tag and parser.has_section("global"):
        tag = parser["global"].get("default")
    tag = tag or "default"
    section = parser[tag] if parser.has_section(tag) else {}
    url = section.get("url") or None          # absent => public github.com
    token = section.get("token") or None
    return url, token


def getGithub() -> Github:
    """ Build a PyGithub client from cmndsControlInfo (serverConfigTag, serverConfigPath). """
    url, token = _githubCfg()
    kwargs = {}
    if url:
        kwargs["base_url"] = url
    if token:
        kwargs["auth"] = Auth.Token(token)
    return Github(**kwargs)


@dataclass
class RepoRef:
    """ Brand-neutral repo descriptor used by all gitist commands. """
    namespacePath: str          # on-disk relative path (gitlab path_with_namespace / github full_name)
    httpUrl: str
    sshUrl: str
    private: bool = False
    ident: object = None        # provider id (gitlab project id / github repo id)


def _brand():
    return gitist_seedInfo.cmndsControlInfo.brand


def _gitlabProjectToRef(proj) -> RepoRef:
    return RepoRef(
        namespacePath=proj.path_with_namespace,
        httpUrl=proj.http_url_to_repo,
        sshUrl=proj.ssh_url_to_repo,
        private=(proj.visibility != "public"),
        ident=proj.id,
    )


def _githubRepoToRef(repo) -> RepoRef:
    return RepoRef(
        namespacePath=repo.full_name,
        httpUrl=repo.clone_url,
        sshUrl=repo.ssh_url,
        private=repo.private,
        ident=repo.id,
    )


def listRepos(namePath: str) -> list:
    """ List repos under an account path -> [RepoRef]. Brand-dispatched. """
    brand = _brand()
    if brand == gitist_seedInfo.GitProviderBrand.Gitlab:
        group = getGitlab().groups.get(namePath)
        return [_gitlabProjectToRef(p) for p in group.projects.list(get_all=True)]
    if brand == gitist_seedInfo.GitProviderBrand.Github:
        gh = getGithub()
        try:
            owner = gh.get_organization(namePath)      # try org first
        except github.GithubException:
            owner = gh.get_user(namePath)              # fall back to user
        return [_githubRepoToRef(r) for r in owner.get_repos()]
    raise NotImplementedError(f"listRepos not implemented for brand {brand}")


def getRepo(repoPath: str) -> RepoRef:
    """ Resolve a single repo by full path -> RepoRef. Brand-dispatched. """
    brand = _brand()
    if brand == gitist_seedInfo.GitProviderBrand.Gitlab:
        return _gitlabProjectToRef(getGitlab().projects.get(repoPath))
    if brand == gitist_seedInfo.GitProviderBrand.Github:
        return _githubRepoToRef(getGithub().get_repo(repoPath))
    raise NotImplementedError(f"getRepo not implemented for brand {brand}")


def authToken():
    """ The access token for the current brand (for https-auth clone URLs). """
    brand = _brand()
    if brand == gitist_seedInfo.GitProviderBrand.Gitlab:
        return getGitlab().private_token
    if brand == gitist_seedInfo.GitProviderBrand.Github:
        return _githubCfg()[1]
    raise NotImplementedError(f"authToken not implemented for brand {brand}")


def _httpsCredPrefix(token) -> str:
    """ Userinfo to inject into an https clone URL, per brand. """
    brand = _brand()
    if brand == gitist_seedInfo.GitProviderBrand.Gitlab:
        return f"oauth2:{token}@"
    if brand == gitist_seedInfo.GitProviderBrand.Github:
        return f"{token}@"
    raise NotImplementedError(f"_httpsCredPrefix not implemented for brand {brand}")


def cloneUrlForRef(ref: RepoRef) -> str:
    """ Choose the clone URL for a RepoRef per cmndsControlInfo access policy. """
    ci = gitist_seedInfo.cmndsControlInfo
    GAT = gitist_seedInfo.GitAccessType
    GAM = gitist_seedInfo.GitAuthAccessMethod

    if ci.gitAccessType == GAT.Auth:
        if ci.gitAuthAccessMethod in (GAM.Ssh, GAM.SshOverHttps):
            if ci.gitAccessAcct:                                # host -> ~/.ssh/config alias
                pathPart = ref.sshUrl.partition('@')[2].partition(':')[2]
                return f"git@{ci.gitAccessAcct}:{pathPart}"
            return ref.sshUrl
        if ci.gitAuthAccessMethod == GAM.Https:
            token = authToken()
            if token and ref.httpUrl.startswith("https://"):
                return ref.httpUrl.replace("https://", f"https://{_httpsCredPrefix(token)}", 1)
            return ref.httpUrl

    return ref.httpUrl                                          # anon => public https


def cloneRef(ref: RepoRef, baseDir: pathlib.Path) -> dict:
    """ Clone one repo under baseDir/namespacePath; skip if it already exists. """
    dest = baseDir / ref.namespacePath
    if dest.exists():
        print(f"skipped (exists): {dest}")
        return {"path": ref.namespacePath, "dest": str(dest), "status": "skipped"}

    url = cloneUrlForRef(ref)
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"cloning: {ref.namespacePath} -> {dest}")
    completed = subprocess.run(
        ["git", "clone", url, str(dest)],
        capture_output=True, text=True,
    )
    if completed.returncode != 0:
        log.error(f"clone failed for {ref.namespacePath}: {completed.stderr.strip()}")
        return {"path": ref.namespacePath, "dest": str(dest), "status": "failed"}
    return {"path": ref.namespacePath, "dest": str(dest), "status": "cloned"}


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitist_reposList" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitist_reposList>>  =verify= argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitist_reposList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
gitlab-pub-gitist.pcs -i gitist_reposList mohsen.byname-group
  #+end_src
#+RESULTS:
: 79388111 mohsen.byname-group/mohsen.byname-project
: [{'id': 79388111, 'path': 'mohsen.byname-group/mohsen.byname-project'}]
        #+end_org """)

        cmndArgs = self.cmndArgsGet("0&1", cmndArgsSpecDict, argsList)
        if not cmndArgs:
            log.error("A gitlab group path argument is required.")
            return failed(cmndOutcome)
        groupPath = cmndArgs[0]

        repos = []
        for ref in listRepos(groupPath):
            print(ref.ident, ref.namespacePath)
            repos.append({"id": ref.ident, "path": ref.namespacePath})

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=repos,
        )


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&1",
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="GroupPath"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitist_reposClone" :comment "" :extent "verify" :ro "cli" :parsMand "destBaseDir" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitist_reposClone>>  =verify= parsMand=destBaseDir argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitist_reposClone(cs.Cmnd):
    cmndParamsMandatory = [ 'destBaseDir', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             destBaseDir: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'destBaseDir': destBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Clone every repo of a gitlab group under destBaseDir (mirroring path_with_namespace; skip if exists).
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
gitlab-pub-gitist.pcs -i gitist_reposClone --destBaseDir=/tmp/gitistTest mohsen.byname-group
  #+end_src
#+RESULTS:
: cloning: mohsen.byname-group/mohsen.byname-project -> /tmp/gitistTest/mohsen.byname-group/mohsen.byname-project
: [{'path': 'mohsen.byname-group/mohsen.byname-project', 'dest': '/tmp/gitistTest/mohsen.byname-group/mohsen.byname-project', 'status': 'cloned'}]
        #+end_org """)

        cmndArgs = self.cmndArgsGet("0&1", cmndArgsSpecDict, argsList)
        if not cmndArgs:
            log.error("A gitlab group path argument is required.")
            return failed(cmndOutcome)
        groupPath = cmndArgs[0]

        baseDir = pathlib.Path(destBaseDir).expanduser()

        results = [cloneRef(ref, baseDir) for ref in listRepos(groupPath)]

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=results,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&1",
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="GroupPath"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitist_clone" :comment "" :extent "verify" :ro "cli" :parsMand "destBaseDir" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitist_clone>>  =verify= parsMand=destBaseDir argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitist_clone(cs.Cmnd):
    cmndParamsMandatory = [ 'destBaseDir', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             destBaseDir: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'destBaseDir': destBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Clone a single gitlab project (by full path) under destBaseDir (mirroring path_with_namespace; skip if exists).
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
gitlab-pub-gitist.pcs -i gitist_clone --destBaseDir=/tmp/gitistTest mohsen.byname-group/mohsen.byname-project
  #+end_src
#+RESULTS:
: cloning: mohsen.byname-group/mohsen.byname-project -> /tmp/gitistTest/mohsen.byname-group/mohsen.byname-project
: {'path': 'mohsen.byname-group/mohsen.byname-project', 'dest': '/tmp/gitistTest/mohsen.byname-group/mohsen.byname-project', 'status': 'cloned'}
        #+end_org """)

        cmndArgs = self.cmndArgsGet("0&1", cmndArgsSpecDict, argsList)
        if not cmndArgs:
            log.error("A gitlab project path argument is required.")
            return failed(cmndOutcome)
        projectPath = cmndArgs[0]

        baseDir = pathlib.Path(destBaseDir).expanduser()
        result = cloneRef(getRepo(projectPath), baseDir)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=result,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&1",
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="ProjectPath"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:

# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for Unbound, BISOS's local resolver (.intra via Knot).
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
** This File: /bisos/git/bxRepos/bisos-pip/dnsCap/py3/bisos/dnsCap/dnsCap_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/dnsCap/py3/bisos/dnsCap/dnsCap_csu.py
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
csInfo['panel'] = 'dnsCap_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This is a =Cs-Unit= for Unbound, BISOS's local resolver. bisos.conf, resolv.conf, the
NetworkManager files and the browser policies are generated from bisos.dnsCap.unboundInfo.
resolv.conf is switched to Unbound only after Unbound has answered; resolverRevert undoes it.

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

import collections
import typing
import subprocess

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

from bisos.dnsCap import unboundInfo as unboundInfoMod
from bisos.dnsCap.unboundInfo import unboundInfo

import pathlib

import logging
log = logging.getLogger(__name__)


####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/  [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
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
    pass


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :comment "~CSU Specification~" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  ~CSU Specification~ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of the Unbound (local resolver) Cmnds.
    #+end_org """

    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert

    if sectionTitle == 'default':
        cs.examples.menuChapter(f'*Unbound -- Local Resolver ({unboundInfo.mode.value}), .intra via Knot*')

    cs.examples.menuSection('/Generate -- to stdout, nothing written/')
    cmnd('unboundConfStdout', comment=f"# {unboundInfo.confFile}")
    cmnd('resolvConfStdout', comment=f"# {unboundInfo.resolvConf} once switched")
    cmnd('nmDispatcherStdout', comment="# the NetworkManager company/VPN domains forwarder")
    cmnd('browserPoliciesStdout', comment="# Firefox and Chrome/Chromium DNS-over-HTTPS off")

    cs.examples.menuSection('/Publish (sudo) -- in this order; unboundFullUpdate does all three/')
    cmnd('unboundConfUpdate', comment="# install if changed, unbound-checkconf, restart, health check")
    cmnd('resolverSwitch', comment="# only if Unbound answers: NetworkManager dns=none, resolv.conf -> 127.0.0.1")
    cmnd('browserPoliciesUpdate', comment="# Firefox policies.json key + Chrome/Chromium managed policy files")
    cmnd('unboundFullUpdate', comment="# the three above")

    cs.examples.menuSection('/Undo/')
    cmnd('resolverRevert', comment=f"# restore {unboundInfo.resolvConfOrig}, drop NetworkManager dns=none")

    cs.examples.menuSection('/Observe/')
    cmnd('unboundStatus', comment="# unbound.service, unbound-control status, forward zones")
    cmnd('unboundQuery', args=unboundInfo.healthCheckName, comment="# kdig @127.0.0.1, answer only")
    literal("kdig @127.0.0.1 debian.org +dnssec   # the ad flag: validated")
    literal("kdig @127.0.0.1 dnssec-failed.org    # SERVFAIL: a deliberately broken signature")
    literal(f"kdig @127.0.0.1 {unboundInfo.firefoxCanary}   # NXDOMAIN: Firefox's DoH canary")
    literal(f"sudo unbound-control -s {unboundInfo.controlSocket} list_forwards")


####+BEGIN: bx:cs:py3:section :title "Publishing -- bash that validates and installs generated files"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Publishing -- bash that validates and installs generated files*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

def _healthCheck() -> str:
    """Bash: Unbound must answer within ~10s, or the script fails. Guards resolverSwitch."""
    return f"""
for i in 1 2 3 4 5 ; do
    if [ -n "$(kdig @127.0.0.1 {unboundInfo.healthCheckName} A +short +time=2 2>/dev/null)" ] ; then
        echo "unbound: answers ({unboundInfo.healthCheckName})"
        healthy=yes
        break
    fi
    sleep 2
done
if [ "$healthy" != yes ] ; then
    echo "unbound: does NOT answer for {unboundInfo.healthCheckName}" >&2
    exit 1
fi
"""


def confPublishScript() -> str:
    """Bash: install bisos.conf if changed; unbound-checkconf the whole set, restoring the
    previous bisos.conf if it fails; restart; health check.

    unbound-checkconf validates unbound.conf with its includes, so the new file is checked
    in place --- and rolled back --- rather than in a temporary location.
    """
    conf = unboundInfo.confFile
    return f"""
set -e
tmpConf=$(mktemp)
trap 'rm -f "$tmpConf"' EXIT
cat > "$tmpConf" <<'BISOS_UNBOUNDCONF_EOF'
{unboundInfoMod.unboundConfContent()}BISOS_UNBOUNDCONF_EOF
if sudo cmp -s "$tmpConf" {conf} 2>/dev/null && systemctl is-active --quiet unbound ; then
    echo "bisos.conf: unchanged, unbound running"
else
    [ -f {conf} ] && sudo cp -p {conf} {conf}.prev
    sudo install -o root -g root -m 644 "$tmpConf" {conf}
    if ! sudo unbound-checkconf ; then
        echo "unbound-checkconf failed: restoring the previous bisos.conf" >&2
        if [ -f {conf}.prev ] ; then sudo mv {conf}.prev {conf} ; else sudo rm -f {conf} ; fi
        exit 1
    fi
    echo "bisos.conf: installed {conf}"
    sudo systemctl enable unbound >/dev/null 2>&1
    sudo systemctl restart unbound
fi
{_healthCheck()}"""


def resolverSwitchScript() -> str:
    """Bash: point this host at Unbound --- only after it has answered.

    NetworkManager first (dns=none, so it stops rewriting resolv.conf), then resolv.conf,
    whose original --- a file or a symlink --- is kept once with cp -P. Hosts without
    NetworkManager (servers) skip its part.
    """
    i = unboundInfo
    return f"""
set -e
{_healthCheck()}
if [ -x /sbin/resolvconf ] ; then
    echo "WARNING: resolvconf is installed and may rewrite {i.resolvConf}" >&2
fi
if [ -d /etc/NetworkManager ] ; then
    sudo install -d -m 755 {i.nmConfFile.parent} {i.nmDispatcherFile.parent}
    sudo tee {i.nmConfFile} >/dev/null <<'BISOS_NMCONF_EOF'
{unboundInfoMod.nmConfContent()}BISOS_NMCONF_EOF
    sudo tee {i.nmDispatcherFile} >/dev/null <<'BISOS_NMDISP_EOF'
{unboundInfoMod.nmDispatcherContent()}BISOS_NMDISP_EOF
    sudo chmod 755 {i.nmDispatcherFile}
    sudo systemctl reload NetworkManager 2>/dev/null || true
    echo "NetworkManager: dns=none, dispatcher installed"
fi
[ -e {i.resolvConfOrig} ] || [ -L {i.resolvConfOrig} ] || sudo cp -P {i.resolvConf} {i.resolvConfOrig}
sudo rm -f {i.resolvConf}
sudo tee {i.resolvConf} >/dev/null <<'BISOS_RESOLV_EOF'
{unboundInfoMod.resolvConfContent()}BISOS_RESOLV_EOF
sudo chmod 644 {i.resolvConf}
echo "resolv.conf: -> 127.0.0.1 (original kept as {i.resolvConfOrig})"
getent ahosts {i.healthCheckName} >/dev/null && echo "getent: {i.healthCheckName} resolves through unbound"
"""


def resolverRevertScript() -> str:
    """Bash: undo resolverSwitch. Unbound keeps running, unused; the browser policies stay."""
    i = unboundInfo
    return f"""
set -e
if [ -e {i.resolvConfOrig} ] || [ -L {i.resolvConfOrig} ] ; then
    sudo rm -f {i.resolvConf}
    sudo mv {i.resolvConfOrig} {i.resolvConf}
    echo "resolv.conf: original restored"
else
    echo "resolv.conf: no {i.resolvConfOrig} -- nothing to restore"
fi
sudo rm -f {i.nmConfFile} {i.nmDispatcherFile}
sudo systemctl reload NetworkManager 2>/dev/null || true
"""


def browserPoliciesScript() -> str:
    """Bash: Firefox's policies.json (BISOS's key merged into it) and Chrome/Chromium's own files."""
    i = unboundInfo
    existing = None
    if i.firefoxPolicies.exists():
        existing = subprocess.run(["sudo", "cat", str(i.firefoxPolicies)],
                                  capture_output=True, text=True).stdout
    chrome = "".join(f"""
sudo install -d -m 755 {path.parent}
sudo tee {path} >/dev/null <<'BISOS_CHROME_EOF'
{unboundInfoMod.chromePolicyContent()}BISOS_CHROME_EOF
sudo chmod 644 {path}
echo "chrome policy: {path}"
""" for path in i.chromePolicyFiles)
    return f"""
set -e
sudo install -d -m 755 {i.firefoxPolicies.parent}
sudo tee {i.firefoxPolicies} >/dev/null <<'BISOS_FIREFOX_EOF'
{unboundInfoMod.firefoxPoliciesMerged(existing)}BISOS_FIREFOX_EOF
sudo chmod 644 {i.firefoxPolicies}
echo "firefox policy: {i.firefoxPolicies}"
{chrome}"""


def _run(cmndOutcome: b.op.Outcome, script: str) -> b.op.Outcome:
    if b.subProc.WOpW(invedBy=None, log=1).bash(script).isProblematic():
        return b_io.eh.badOutcome(cmndOutcome)
    return cmndOutcome.set(opError=b.OpError.Success)


def fullUpdate(cmndOutcome: b.op.Outcome) -> b.op.Outcome:
    """Unbound first; the switch only if it answers (its script re-checks); then the browsers."""
    for script in (confPublishScript, resolverSwitchScript, browserPoliciesScript):
        if _run(cmndOutcome, script()).isProblematic():
            return cmndOutcome
    return cmndOutcome


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Unbound Cmnds"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Unbound Cmnds  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "unboundConfStdout" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<unboundConfStdout>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class unboundConfStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print bisos.conf as it would be generated. Writes nothing.
        #+end_org """): return(cmndOutcome)

        content = unboundInfoMod.unboundConfContent()
        print(content, end="")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "resolvConfStdout" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<resolvConfStdout>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class resolvConfStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print /etc/resolv.conf as it would be after resolverSwitch. Writes nothing.
        #+end_org """): return(cmndOutcome)

        content = unboundInfoMod.resolvConfContent()
        print(content, end="")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "nmDispatcherStdout" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<nmDispatcherStdout>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class nmDispatcherStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the NetworkManager dispatcher (company/VPN domains forwarder). Writes nothing.
        #+end_org """): return(cmndOutcome)

        content = unboundInfoMod.nmDispatcherContent()
        print(content, end="")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "browserPoliciesStdout" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<browserPoliciesStdout>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class browserPoliciesStdout(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the Firefox and Chrome/Chromium policies (Firefox's shown unmerged). Writes nothing.
        #+end_org """): return(cmndOutcome)

        content = unboundInfoMod.firefoxPoliciesMerged(None) + unboundInfoMod.chromePolicyContent()
        print(content, end="")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "unboundConfUpdate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<unboundConfUpdate>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class unboundConfUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Install bisos.conf if changed, unbound-checkconf (rolls back on failure), restart, health check.
        #+end_org """): return(cmndOutcome)

        return _run(cmndOutcome, confPublishScript())


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "resolverSwitch" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<resolverSwitch>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class resolverSwitch(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Only if Unbound answers: NetworkManager dns=none + dispatcher, resolv.conf -> 127.0.0.1.
        #+end_org """): return(cmndOutcome)

        return _run(cmndOutcome, resolverSwitchScript())


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "browserPoliciesUpdate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<browserPoliciesUpdate>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class browserPoliciesUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Firefox policies.json (key merged) and Chrome/Chromium managed policy files: DoH off.
        #+end_org """): return(cmndOutcome)

        return _run(cmndOutcome, browserPoliciesScript())


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "unboundFullUpdate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<unboundFullUpdate>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class unboundFullUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  unboundConfUpdate, then resolverSwitch, then browserPoliciesUpdate.
        #+end_org """): return(cmndOutcome)

        return fullUpdate(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "resolverRevert" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<resolverRevert>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class resolverRevert(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Undo resolverSwitch: restore the original resolv.conf, drop NetworkManager dns=none.
        #+end_org """): return(cmndOutcome)

        return _run(cmndOutcome, resolverRevertScript())


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "unboundStatus" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<unboundStatus>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class unboundStatus(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  unbound.service, unbound-control status and forward zones. Read-only.
        #+end_org """): return(cmndOutcome)

        return _run(cmndOutcome, f"""
systemctl is-active unbound || true
sudo unbound-control -s {unboundInfo.controlSocket} status 2>&1 || true
sudo unbound-control -s {unboundInfo.controlSocket} list_forwards 2>&1 || true
sudo unbound-control -s {unboundInfo.controlSocket} list_stubs 2>&1 || true
""")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "unboundQuery" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<unboundQuery>>  =verify= argsMin=1 argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class unboundQuery(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 2,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Ask the local Unbound: kdig @127.0.0.1 <name> [type], answer only.
        #+end_org """): return(cmndOutcome)

        cmndArgs = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        name = cmndArgs[0]
        rrType = cmndArgs[1] if len(cmndArgs) > 1 else "A"
        result = subprocess.run(["kdig", "@127.0.0.1", name, rrType, "+short"], capture_output=True, text=True)
        print(result.stdout, end="")
        if result.returncode != 0:
            b_io.ann.note(f"unboundQuery: kdig failed: {result.stderr.strip()}")
            return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=result.stdout.strip())

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="name [rrType], rrType defaults to A"
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

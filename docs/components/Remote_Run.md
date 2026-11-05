# ![](/images/icons/Remote_Run.png) Remote Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Remote%20Run%22)

![](/images/components/Remote_Run-crop.png)

Run a written wind study on another machine over SSH (a workstation, server or cloud VM with Eddy3D's CLI and a container engine). Submit packages the study's static part, copies it to <Remote Folder>/<study>-<time> under the remote home and starts `E3D run` detached; while it runs the component polls every minute and shows each direction's convergence; Fetch copies the solved study back over the local one. SSH uses key login only and never prompts: connect once in a terminal first. The remote must be Linux, macOS or WSL.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Study |  | The Wind Study (Outdoor Case output) or the study folder path. | `Generic Data` |
| Host |  | user@host or an ~/.ssh/config alias. | `Text` |
| Remote Folder | Folder | Folder under the remote home that holds the jobs. | `Text` |
| Remote CLI | CLI | Eddy3D's CLI on the remote; an absolute path when a non-interactive ssh shell does not have E3D on PATH. | `Text` |
| Parallel |  | MPI ranks for the remote run; 0 = what the study is decomposed for. | `Integer` |
| Attempts |  | Numerics ladder attempts per direction (1-5), as `E3D run --attempts`. | `Integer` |
| Watch Port | Port | 0 = none. Otherwise also serve a read-only progress page on the remote's loopback port; the Tunnel output is the ssh command that opens it here at http://localhost:<port>. | `Integer` |
| Submit |  | Package, upload and start the remote run. | `Boolean` |
| Fetch |  | Copy the solved study back over the local one. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Status |  | Running, Finished, FinishedUnconverged, Failed, Lost or Unreachable. | `Text` |
| Directions | Dirs | Each direction case and its convergence verdict on the remote. | `Text` |
| Log |  | The tail of the remote run.log, then this component's own steps. | `Text` |
| Tunnel |  | The ssh command that makes the remote progress page http://localhost:<port>. | `Text` |
| Study Folder | Folder | The local study folder (Fetch writes into it). | `Text` |
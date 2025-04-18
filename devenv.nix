{ pkgs, lib, config, inputs, ... }:

{
  packages = [ pkgs.git ];
  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.uv.enable = true;
  enterShell = ''
    git --version
  '';
  # See full reference at https://devenv.sh/reference/options/
}

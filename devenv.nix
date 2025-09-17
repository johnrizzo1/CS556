{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ git ];
  languages.python.enable = true;
  languages.python.version = "3.12";
  languages.python.venv.enable = true;
  languages.python.uv.enable = true;
  # See full reference at https://devenv.sh/reference/options/
}

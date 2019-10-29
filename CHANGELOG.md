# Changelog
All noteable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.13.0] - 2019-10-29
### Changed
- Moved "Meow" to a speak command, provided more options.
- Altered room "Bedroom" to add a sleeping human in description and bool for sleeping

## [0.12.0] - 2019-06-10
### Added
- ability to say "Meow!" as a command

## [0.11.0] - 2019-06-05
### Changed
- Show descriptions to modify used_look
- Move command to be one function
- Current room to be consistently spaced by underscore

## [0.10.0] - 2019-06-05
### Added
- exitGame function to handle quitting ame
- score variable to hold game score

## [0.9.0] - 2019-06-01
### Changed
- Variable names for used_look and current_room to be consistent with rest of project
- Logic to handle moves to its own function

## [0.8.0] - 2019-05-31
### Added
- movePlayer fuction to avoid duplicate code
- Instructions to README.md to run game

### Changed
- Exit for Living Room to be north to avoid confusion

## [0.7.0] - 2019-05-30
### Added
- Kitchen and Bathroom rooms
- Using l as a shortcut for look

### Changed
- Directions to be a variable
- Look command to not display room name after

## [0.6.1] - 2019-05-29
### Fixed
- Typos introduced to game text by v0.6.0

## [0.6.0] - 2019-05-29
### Added
- Added VS code to gitignore to use that editor

### Changed
- Linted project for PEP8 Standards

## [0.5.0] - 2019-05-28
### Added
- Bonus room to list of available rooms
- Edited docstrings to use double quotes instead of comment format

## [0.4.0] - 2017-12-26
### Added
- Help command to list commands.
- Checks for alternative version of Go and Quit commands

## [0.3.0] - 2017-12-26
### Added
- Descriptions to rooms and a showDescription command to display them

### Fixed
- Typo so now showStatus displays "You are in X room"
- Numbering in CHANGELOG.md

## [0.2.0] - 2017-9-25
### Added
- Color through ANSI escape sequences: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

### Changed
- Altered README.md for requirements and synopsis
- Altered .gitignore for venv
- Replaced raw_input with input for Python3 compliance

### Fixed
- Bug with invalid command being issued for commands other than `quit`

## [0.1.0] - 2017-9-22
### Added
- MIT license

### Changed
- Altered README.md with badges and links to license and changelog

## 0.0.0 - 2017-9-22
### Added
- Basic game loop
- 'Go' and 'Quit' commands
- .gitignore
- Changelog and Readme files

[Unreleased]: https://github.com/afs2015/PepperRPG/compare/v0.13.0....HEAD
[0.13.0]: https://github.com/afs2015/PepperRPG/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/afs2015/PepperRPG/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/afs2015/PepperRPG/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/afs2015/PepperRPG/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/afs2015/PepperRPG/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/afs2015/PepperRPG/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/afs2015/PepperRPG/compare/v0.6.1...v0.7.0
[0.6.1]: https://github.com/afs2015/PepperRPG/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/afs2015/PepperRPG/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/afs2015/PepperRPG/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/afs2015/PepperRPG/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/afs2015/PepperRPG/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/afs2015/PepperRPG/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/afs2015/PepperRPG/compare/v0.0.0...v0.1.0

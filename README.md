# Cat Memory Game

The application is a simple memory game where the player is presented with a grid of cards. The objective of the game is to flip over pairs of cards and match them to reveal their images.

## Documentation

- [Requirement Specification](https://github.com/ElliJohansson/memory-game/blob/master/documentation/requirement_specification.md)
- [Instructions](https://github.com/ElliJohansson/memory-game/blob/master/documentation/instructions.md)
- [Work Time log](https://github.com/ElliJohansson/memory-game/blob/master/documentation/work_time_log.md)
- [Changelog](https://github.com/ElliJohansson/memory-game/blob/master/documentation/changelog.md)  
- [Architecture](https://github.com/ElliJohansson/memory-game/blob/master/documentation/architecture.md)
- [Testing document](https://github.com/ElliJohansson/memory-game/blob/master/documentation/testing_document.md)
- [References](https://github.com/ElliJohansson/memory-game/blob/master/documentation/references.md)
- [Release](https://github.com/ElliJohansson/memory-game/releases/tag/viikko5)


## Command-line operations

Install dependencies:
```
poetry install
``` 
Start the program:
```
poetry run invoke start
```
Run tests:
```
poetry run invoke test
```
Generate test coverage:
```
poetry run invoke coverage-report
```
_The report will be generated in the htmlcov directory._

Run pylint:
```
poetry run invoke lint
``` 

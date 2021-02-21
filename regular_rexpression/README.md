# Regular Expressions

## Character Classes

### Commin Character Classes

| Class | Description                                                               |
| ---   | ---                                                                       |
| `\d`  | One digit from 0 to 9.                                                    |
| `\w`  | Word character: ASCII letter, digit, or underscore.                       |
| `\s`  | Whitespace character: space, tab, newline, carriage return, vertical tab. |

An upper case version of any of those classes represents the complement of the
class. For example, `\d` represents anything that is not a digit.

### White-Space Classes

| Class  | Description               |
| ---    | ---                       |
| `\t`   | Tab                       |
| `\v`   | Vertical tab              |
| `\r`   | Carriage return character |
| `\n`   | Line feed character       |
| `\r\n` | Line separator on Windows |

### Custom Character Classes

| Class     | Description                                                                 | Example                                 |
| ---       | ---                                                                         | --                                      |
| `[…]`     | Starts a character class.                                                   | `[m-q]` Any lowercase letter fro m to q |
| `[^…]`    | Negates a character class.                                                  | `[^\w]` Any non-word character          |
| `[…-[…]]` | One character that is in those on the left, but not in the subtracted class | `[a-z-[aeiou]]` Any lowercase consonant |

### Special Characters

- `.`: Any character except line break.
- `\`: `\` followed by any of `[\^$.?\@*+(){}` suppress their special meaning.

## Quantifiers

| Quantifier | Description                                                               |
| ---        | ---                                                                       |
| `+`        | One or more. The `+` is "greedy".                                         |
| `*`        | Zero or more times. The `*` is "greedy".                                  |
| `?`        | Once or none. `?` makes a quantifier lazy. `??` makes `?` lazy.           |
| `{3}`      | Exactly three times.                                                      |
| `{2,4}`    | Two to four times. It is greedy by default. Append `?` to make it lazy.   |
| `{3,}`     | Three or more times. It is greedy by default. Append `?` to make it lazy. |

## Anchors

| Anchor | Description                                                                                           |
| ---    | ---                                                                                                   |
| `^`    | Start of string or start of line depending on multiline mode.                                         |
| `$`    | End of string or end of line depending on multiline mode.                                             |
| `\A`   | Beginning of string. Matches a position rather than a character. Never matches after line breaks.     |
| `\z`   | Very end of the string. Matches a position rather than a character. Never matches before line breaks. |
| `\b`   | Word boundary (position where one side only is an ASCII letter, digit or underscore) .                |
| `\Q…\E`   | Matches the characters between \Q and \E literally, suppressing the meaning of special characters. |

## Logic

| Character | Description              |
| ---       | ---                      |
| `@`       | Alternation / OR operand |
| `(…)`     | Capturing group          |
| `\1`      | Contents of Group 1      |
| `\2`      | Contents of Group 2      |
| `(?: … )` | Non-capturing group      |


## Inline modifiers

| Character | Description                                                                                                   |
| ---       | ---                                                                                                           |
| `(?i)`    | Turn on case insensitivity for the remainder of the regular expression. `(?-i)` turns off case insensitivity. |
| `(?s)`    | Turn on "dot matches newline" for the remainder of the regular expression.                                     |

## Atomic Grouping

- `(?>regex)`: Atomic groups prevent the regex engine from backtracking back
  into the group (forcing the group to discard part of its match) after a match
  has been found for the group.

## Lookarounds

| Character | Description                    | Example                                            |
| ---       | ---                            | ---                                                |
| `(?=…)`   | Zero-width positive lookahead  | `t(?=s)`      Matches the second `t` in `streets`  |
| `(?<=…)`  | Zero-width positive lookbehind | `t(?!s)`      Matches the first `t` in `streets`.  |
| `(?!…)`   | Zero-width negative lookahead  | `(?<=s)t`     Matches the first `t` in `streets`.  |
| `(?<!…)`  | Zero-width negative lookbehind | `(?<!s)t`     Matches the second `t` in `streets`. |

## Conditionals

| Character               | Description |
| ---                     | ---         |
| `(?(?=regex)then@else)` |             |
| `(?(1)then@else)`       |             |

# Vim Syntax

| Perl          | Magic                       | Very Magic                 | Description                                   |
| ---           | ---                         | ---                        | ---                                           |
| `x?`          | `x\=`, `x\?`                | `x=`, `x?`                 | Match 0 or 1 of `x`                           |
| `x*`          | `x\*`                       | `x*`                       | Match 0 or more of `x` (greedy)               |
| `x+`          | `x\+`                       | `x+`                       | Match 1 or more of `x` (greedy)               |
| `x{n}`        | `x\{n}`                     | `x{n}`                     | Match exactly n of `x`                        |
| `x{n,m}`      | `x\{n,m}`                   | `x{n,m}`                   | Match n to m of `x` (greedy)                  |
| `x{n,m}?`     | `x\{-n,m}`                  | `x{-n,m}`                  | Match n to m of `x` (non-greedy)              |
| `*?`          | `\{-}`                      | `{-}`                      | Lazy `*`                                      |
| `+?`          | `\{-1,}`                    | `{-1,}`                    | Lazy `+`                                      |
| `x*?`         | `x\{-}`                     | `x{-}`                     | Match 0 or 1 of `x` (non-greedy)              |
| `x+?`         | `x\{-1,}`                   | `x{-1,}`                   | Match 1 or more of `x` (non-greedy)           |
| `(xyz)`       | `\(xyz\)`                   | `(xyz)`                    | Use brackets to group matches                 |
| `\b`          | `\<…\>`                     | `<…>`                      | Word boundaries                               |
| `\1` ... `\9` | `\1` ... `\9`               | `\1` ... `\9`              | Backreferences for previously grouped matches |
| `[\w]`        | `[[:alnum:]]`               | `[[:alnum:]]`              | Word character inside `[]`                    |
| `[\d]`        | `[[:digit:]]`               | `[[:digit:]]`              | Digit character inside `[]`                   |
| `[\t]`        | `[\t]`                      | `[\t]`                     | Tab character inside `[]`                     |
| `[\r\n]`      | ` [\r\n]`                   | `[\r\n]`                   | Newline character inside `[]`                 |
| `(?i)`        | `\c`                        | `\c`                       | Turn on case insensitivity                    |
| `(?-i)`       | `\C`                        | `\C`                       | Turn off case insensitivity                   |
| `(?m)`        | `\_.`                       | `\_.`                      | Dot matches multiline                         |
| `(?:regex)`   | `\%(regex\)`                | `%(regex)`                 | Non-matching group                            |
| `(?=regex)`   | `(regex)\@=`, `\ze(regex)`  | `(regex)@=`, `\ze(regex)`  | Positive lookahead                            |
| `(?!regex)`   | `(regex)\@!`                | `(regex)@!`                | Negative lookahead                            |
| `(?<=regex)`  | `(regex)\@<=`, `(regex)\zs` | `(regex)@<=`, `(regex)\zs` | Positive lookbehind                           |
| `(?!regex)`   | `(regex)\@<!`               | `(regex)@<!`               | Negative lookbehind                           |
| `(?>regex)`   | `(regex)\@>`                | `(regex)@>`                | Atomic grouping                               |

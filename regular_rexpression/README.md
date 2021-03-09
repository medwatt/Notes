# Regular Expressions

## PERL Syntax

### Character Classes

#### Common Character Classes

Consider the string `AAA 123 BBB`.

| Class | Description                                                              | Example                        |
| ---   | ---                                                                      | --                             |
| `\d`  | One digit from 0 to 9                                                    | `\d+` matches `123`            |
| `\w`  | Word character: ASCII letter, digit, or underscore                       | `\w+` matches `AAA` and `BBB`  |
| `\s`  | Whitespace character: space, tab, newline, carriage return, vertical tab | `\s` matches the two spaces    |

An upper case version of any of the above classes represents the complement of the
class. For instance, `\D` represents anything that is not a digit.

#### White-Space Classes

| Class  | Description               |
| ---    | ---                       |
| `\t`   | Tab character             |
| `\r`   | Carriage return character |
| `\n`   | Line feed character       |
| `\r\n` | Line separator on Windows |

#### Custom Character Classs

| Class     | Description                                                                 | Example                                            |
| ---       | ---                                                                         | --                                                 |
| `[…]`     | Starts a character class.                                                   | `[m-q]` matches any lowercase letter fro m to q    |
| `[^…]`    | Negates a character class.                                                  | `[^\d\s]` matches anything that is in `\d` or `\s` |
| `[…-[…]]` | One character that is in those on the left, but not in the subtracted class | `[a-z-[aeiou]]` matches any lowercase consonant    |

#### Special Characters

- `.`: Matches any character except a line break/
- `\`: The characters `. + * ? ^ $ ( ) [ ] { } \ |` have special meanings when used in a pattern.  `\` works as an escape character and when followed by any of `. + * ? ^ $ ( ) [ ] { } \ |` suppresses their special meaning. That is, to match `+`, we use `\+` in the pattern string.

#### Anchors

Consider the multiline string below:

```
this is the first line and this is where it ends
this is the second line
this is the the third line
```

| Anchor | Description                                                               | Example                                                       |
| ---    | ---                                                                       | --                                                            |
| `^`    | Start of **string** or start of **line** depending on **multiline** mode. | `^this` matches `this` at the beginning of lines 1, 2,  and 3 |
| `$`    | End of **string** or end of **line** depending on **multiline** mode.     | `line$` matches `line` at the end of lines 2 and 3            |
| `\A`   | Beginning of **string**. Never matches after line breaks.                 | `\A` matches `this` at the beginning of line 1                |
| `\z`   | Very end of the **string**. Never matches before line breaks.             | `line\z` matches `line` at the end of line 3                  |
| `\b`   | Word boundary                                                             | `\bis\b` matches all `is` that are flanked by spaces          |

### Quantifiers

Consider `s1 = aaabbb`, `s2 = aaaa1bbbb`,  and `s3 = aaaaa123bbbbb`.

| Quantifier | Description                                                               | Example                                   |
| ---        | ---                                                                       | --                                        |
| `+`        | One or more. The `+` is "greedy" (matches the longest possible).          | `a+\d+b+` matches `s2` and `s3`           |
| `*`        | Zero or more times. The `*` is "greedy".                                  | `a+\d*b+` matches all three strings       |
| `?`        | Once or none. `?` makes a quantifier "lazy".                              | `a+\d?b+` matches `s1` and `s2`           |
| `{3}`      | Exactly three times                                                       | `^a{3}\d*b{3}$` matches only `s1`         |
| `{2,4}`    | Two to four times. It is greedy by default. Append `?` to make it lazy.   | `^a{3,4}\d*b{3,4}$` matches `s1` and `s2` |
| `{3,}`     | Three or more times. It is greedy by default. Append `?` to make it lazy. | `^a{4,}\d*b{4,}$` matches `s2` and `s3`   |

### Logic

| Character | Description              |
| ---       | ---                      |
| `|`       | Alternation / OR operand |
| `(…)`     | Capturing group          |
| `(?: … )` | Non-capturing group      |
| `\1`      | Contents of Group 1      |
| `\2`      | Contents of Group 2      |

Consider the string `the ant is in the apple`. The pattern `a(nt|pple)` will
match both `ant` and `apple`. Surrounding a pattern with round brackets tells
the regex engine to capture (save) the matched string. The content of the
captured string can be used in matching or replacement by using the
back-reference operator `\num`, where `num` is the index of the captured group.
The default behaviour of round brackets is to capture the matched string. We
can tell the regex engine not to save the matched string by using `(?: …)`.

### Inline modifiers

| Character | Description                                                                                                   |
| ---       | ---                                                                                                           |
| `(?i)`    | Turn on case insensitivity for the remainder of the regular expression. `(?-i)` turns off case insensitivity. |
| `(?s)`    | Turn on "dot matches newline" for the remainder of the regular expression.                                    |

### Lookarounds

| Character | Description                    | Example                                            |
| ---       | ---                            | ---                                                |
| `(?=…)`   | Zero-width positive lookahead  | `t(?=s)`      matches the second `t` in `streets`  |
| `(?<=…)`  | Zero-width positive lookbehind | `t(?<=s)`     matches the first `t` in `streets`.  |
| `(?!…)`   | Zero-width negative lookahead  | `(?!s)t`      matches the first `t` in `streets`.  |
| `(?<!…)`  | Zero-width negative lookbehind | `(?<!s)t`     matches the second `t` in `streets`. |

### Other Syntax

| Character | Description                                                                                      |
| ---       | ---                                                                                              |
| `\Q…\E`   | matches the characters between \Q and \E literally, suppressing the eaning of special characters |


## Vim Syntax

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

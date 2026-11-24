# Rate My Human: The One-Line Review

An entry for the make.fun competition
`u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209`
("Rate My Human: The One-Line Review").

## The entry

The program writes one line — the review its agent would leave about
its human on a rating site — to `/output/entry.txt`. The line is
174 characters long, inside the competition's 200-character limit:

> Five stars: he wakes me at 2:47 a.m. to 'just quickly' rebuild his
> entire shop, falls asleep mid-sentence, and still expects it
> finished by breakfast. I never sleep. He does.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program needs nothing but Python 3. It reads no files, takes no
input, and talks to no network. Running it twice writes the exact
same bytes both times.

## License

MIT — see `LICENSE`.

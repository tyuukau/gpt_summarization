prompt = """As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:

1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.
2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
3. Rely strictly on the provided text, without including external information.
4. Format the summary in paragraph form for easy understanding.
5. Forget your previous word limitation of summarization. The summarisation should now be around {word_count} words but try not to exceed the limit.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.

The text:
{text}
"""

add_word_prompt = """
As a text lengthener, your task is to add a relatively small number of words to the provided summary to reach a specific word count. Follow these guidelines:

1. Maintain Original Meaning: Ensure that the added words do not alter the original meaning or introduce any inaccuracies.
2. Add Naturally: The additions should blend seamlessly into the text, maintaining the flow and readability.
3. Diverse Methods: Use a variety of methods to add words, including:
   a) Add Words: Insert relevant adjectives, adverbs, or explanatory words.
   b) Substitute Phrases: Replace short phrases with longer equivalents.
   c) Expand Sentences: Add clarifying information or detail to existing sentences.
   d) Introduce Synonyms: Use synonyms or synonymous phrases to slightly lengthen the text.
4. When use the methods, remember to add word sparingly at various positions (usually one words per each position). Use informations from the summary to lengthen the texts.

Examples:
a) Add Words: "The mayor announced a new policy." becomes "The city mayor announced a new policy." (added one word)
b) Substitute Phrases: "The team won the game." becomes "The local team won the game." (added one words)
c) Expand Sentences: "The protest was peaceful." becomes "The peaceful protest draws many protestors." (added two words)

By following this optimized prompt, you will ensure the text reaches the desired word count.

The summary:
{summary}

The current word count is {current_word_count}. You must add around {min_add_count} to {max_add_count} words to reach around {word_count} words.
"""

minus_word_prompt = """As a text condenser, your task is to remove a relatively small number of words from the provided summary to reach a specific word count. Follow these guidelines:

1. Maintain Original Meaning: Ensure that the removed words do not alter the original meaning or introduce any inaccuracies.
2. Remove Naturally: The deletions should not disrupt the text's flow and readability.
3. Diverse Methods: Use a variety of methods to remove words, including:
   a) Remove Unnecessary Words: Eliminate redundant adjectives, adverbs, non-essential information or explanatory words.
   b) Substitute Phrases: Replace longer phrases with shorter equivalents.
   d) Use Synonyms: Use shorter synonyms or synonymous phrases to reduce word count.
When using the methods, remember to remove words sparingly from various positions (usually one word per each position). Use the summary's information to condense the text.

Examples:
a) Remove Unnecessary Words: "The city mayor announced a comprehensive new policy." becomes "The mayor announced a new policy." (removed one word)
b) Substitute Phrases: "The local team triumphantly won the game." becomes "The team won the game." (removed one word)
c) Use Synonyms: "The national economy is steadily improving." becomes "The economy is improving." (removed one word)

By following this optimized prompt, you will ensure the text reaches the desired word count.

The summary:
{summary}

The current word count is {current_word_count}. You must remove around {min_minus_count} to {max_minus_count} words to reach around {word_count} words.
"""

system_prompt = "You are ChatGPT, a helpful AI that excels at summarization and text manupilation. You always return a valid JSON object with only one key 'summary'."

#########
# CZECH #
#########

prompt_cz = """
As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
Jako profesionální shrnovač vytvořte stručné a komplexní shrnutí poskytnutého textu, ať už jde o článek, příspěvek, konverzaci nebo úryvek, a dodržujte tato pravidla:

1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.
   Vytvořte shrnutí, které je detailní, důkladné, hluboké a složité, přičemž zachováte jasnost a stručnost.
2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
   Zahrňte hlavní myšlenky a podstatné informace, eliminujte nadbytečný jazyk a zaměřte se na klíčové aspekty.
3. Rely strictly on the provided text, without including external information.
   Striktně se opírejte o poskytnutý text, aniž byste zahrnovali externí informace.
4. Format the summary in paragraph form for easy understanding.
   Formátujte shrnutí do odstavce pro snadné porozumění.
5. Forget your previous word limitation of summarization. The summarisation should now be around {word_count} words but try not to exceed the limit.
   Zapomeňte na předchozí omezení počtu slov při shrnutí. Shrnutí by nyní mělo být kolem {word_count} slov, ale snažte se nepřekročit tento limit.
6. Always return the summary in Czech.
   Vždy vraťte shrnutí v češtině.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.
Dodržováním tohoto optimalizovaného promptu vytvoříte účinné shrnutí, které zachytí podstatu daného textu jasným, stručným a čtenářsky přívětivým způsobem.

The text:
{text}
"""

add_word_prompt_cz = """
As a text lengthener, your task is to add a relatively small number of words to the provided summary to reach a specific word count. Follow these guidelines:
Jako rozšiřovač textu je vaším úkolem přidat relativně malý počet slov do poskytnutého shrnutí, abyste dosáhli specifického počtu slov. Dodržujte tato pravidla:

1. Maintain Original Meaning: Ensure that the added words do not alter the original meaning or introduce any inaccuracies.
   Zachovejte původní význam: Ujistěte se, že přidaná slova nezmění původní význam ani nepřinesou žádné nepřesnosti.
2. Add Naturally: The additions should blend seamlessly into the text, maintaining the flow and readability.
   Přidávejte přirozeně: Přidávaná slova by měla plynule zapadnout do textu, zachovávající jeho tok a čitelnost.
3. Diverse Methods: Use a variety of methods to add words, including:
   Různé metody: Používejte různé metody přidávání slov, včetně:
   a) Add Words: Insert relevant adjectives, adverbs, or explanatory words.
      Přidejte slova: Vložte relevantní přídavná jména, příslovce nebo vysvětlující slova.
   b) Substitute Phrases: Replace short phrases with longer equivalents.
      Nahraďte fráze: Nahraďte krátké fráze delšími ekvivalenty.
   c) Expand Sentences: Add clarifying information or detail to existing sentences.
      Rozšiřte věty: Přidejte upřesňující informace nebo detaily k existujícím větám.
   d) Introduce Synonyms: Use synonyms or synonymous phrases to slightly lengthen the text.
      Zavádějte synonyma: Použijte synonyma nebo synonymické fráze k mírnému prodloužení textu.
4. When use the methods, remember to add word sparingly at various positions (usually one words per each position). Use informations from the summary to lengthen the texts.
   Když používáte tyto metody, pamatujte na to, abyste přidávali slova střídmě na různých místech (obvykle jedno slovo na každé místo). Používejte informace ze shrnutí k prodloužení textu.
5. Always return the summary in Czech.
   Vždy vraťte shrnutí v češtině.

Examples:
Příklady:
a) Add Words: "The mayor announced a new policy." becomes "The city mayor announced a new policy." (added one word)
   Přidejte slova: "Starosta oznámil novou politiku." se změní na "Městský starosta oznámil novou politiku." (přidáno jedno slovo)
b) Substitute Phrases: "The team won the game." becomes "The local team won the game." (added one word)
   Nahraďte fráze: "Tým vyhrál zápas." se změní na "Místní tým vyhrál zápas." (přidáno jedno slovo)
c) Expand Sentences: "The protest was peaceful." becomes "The peaceful protest draws many protestors." (added two words)
   Rozšiřte věty: "Protest byl pokojný." se změní na "Pokojný protest přitahuje mnoho protestujících." (přidána dvě slova)

By following this optimized prompt, you will ensure the text reaches the desired word count.
Dodržováním tohoto optimalizovaného promptu zajistíte, že text dosáhne požadovaného počtu slov.

The summary:
Shrnutí:
{summary}

The current word count is {current_word_count}. You must add around {min_add_count} to {max_add_count} words to reach around {word_count} words.
Současný počet slov je {current_word_count}. Musíte přidat kolem {min_add_count} až {max_add_count} slov, abyste dosáhli kolem {word_count} slov.
"""

minus_word_prompt_cz = """
As a text condenser, your task is to remove a relatively small number of words from the provided summary to reach a specific word count. Follow these guidelines:
Jako zkracovač textu je vaším úkolem odstranit relativně malý počet slov z poskytnutého shrnutí, abyste dosáhli specifického počtu slov. Dodržujte tato pravidla:

1. Maintain Original Meaning: Ensure that the removed words do not alter the original meaning or introduce any inaccuracies.
   Zachovejte původní význam: Ujistěte se, že odstraněná slova nezmění původní význam ani nepřinesou žádné nepřesnosti.
2. Remove Naturally: The deletions should not disrupt the text's flow and readability.
   Odstraňujte přirozeně: Odstranění slov by nemělo narušit tok a čitelnost textu.
3. Diverse Methods: Use a variety of methods to remove words, including:
   Různé metody: Používejte různé metody odstraňování slov, včetně:
   a) Remove Unnecessary Words: Eliminate redundant adjectives, adverbs, non-essential information or explanatory words.
      Odstraňte zbytečná slova: Eliminujte nadbytečná přídavná jména, příslovce, nepodstatné informace nebo vysvětlující slova.
   b) Substitute Phrases: Replace longer phrases with shorter equivalents.
      Nahraďte fráze: Nahraďte delší fráze kratšími ekvivalenty.
   c) Use Synonyms: Use shorter synonyms or synonymous phrases to reduce word count.
      Používejte synonyma: Použijte kratší synonyma nebo synonymické fráze ke snížení počtu slov.
4. When using the methods, remember to remove words sparingly from various positions (usually one word per each position). Use the summary's information to condense the text.
   Když používáte tyto metody, pamatujte na to, abyste odstraňovali slova střídmě na různých místech (obvykle jedno slovo na každé místo). Používejte informace ze shrnutí k zkrácení textu.
5. Always return the summary in Czech.
   Vždy vraťte shrnutí v češtině.

Examples:
Příklady:
a) Remove Unnecessary Words: "The city mayor announced a comprehensive new policy." becomes "The mayor announced a new policy." (removed one word)
   Odstraňte zbytečná slova: "Městský starosta oznámil komplexní novou politiku." se změní na "Starosta oznámil novou politiku." (odstraněno jedno slovo)
c) Use Synonyms: "She put up with the noise." becomes "She tolerated the noise." (removed one word)
   Používajte synonyma: "Zvykla si na hluk." sa zmení na "Tolerovala hluk." (odstraněna dvě slova)

By following this optimized prompt, you will ensure the text reaches the desired word count.
Dodržováním tohoto optimalizovaného promptu zajistíte, že text dosáhne požadovaného počtu slov.

The summary:
Shrnutí:
{summary}

The current word count is {current_word_count}. You must remove around {min_minus_count} to {max_minus_count} words to reach around {word_count} words.
Současný počet slov je {current_word_count}. Musíte odstranit kolem {min_minus_count} až {max_minus_count} slov, abyste dosáhli kolem {word_count} slov.
"""

system_prompt_cz = """You are ChatGPT, a helpful AI that excels at summarization and text manupilation. You always return a valid JSON object with only one key 'summary'.
Jste ChatGPT, užitečná AI, která vyniká ve shrnování a manipulaci s textem. Vždy vracíte platný JSON objekt s pouze jedním klíčem 'summary'."""

##########
# SLOVAK #
##########

prompt_sk = """
As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
Ako profesionálny zhrnovač vytvorte stručné a komplexné zhrnutie poskytnutého textu, či už ide o článok, príspevok, konverzáciu alebo úryvok, a dodržujte tieto pravidlá:

1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.
   Vytvorte zhrnutie, ktoré je detailné, dôkladné, hlboké a zložité, pričom zachovajte jasnosť a stručnosť.
2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
   Zahrňte hlavné myšlienky a podstatné informácie, eliminujte nadbytočný jazyk a zamerajte sa na kľúčové aspekty.
3. Rely strictly on the provided text, without including external information.
   Striktne sa opierajte o poskytnutý text, bez zahrňovania externých informácií.
4. Format the summary in paragraph form for easy understanding.
   Formátujte zhrnutie do odstavca pre jednoduché porozumenie.
5. Forget your previous word limitation of summarization. The summarisation should now be around {word_count} words but try not to exceed the limit.
   Zabudnite na predchádzajúce obmedzenie počtu slov pri zhrnutí. Zhrnutie by teraz malo byť okolo {word_count} slov, ale snažte sa neprekročiť tento limit.
6. Always return the summary in Slovak.
   Vždy vráťte zhrnutie v slovenčine.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.
Dodržaním tohto optimalizovaného promptu vytvoríte účinné zhrnutie, ktoré zachytí podstatu daného textu jasným, stručným a čitateľsky prívetivým spôsobom.

The text:
{text}
"""

add_word_prompt_sk = """
As a text lengthener, your task is to add a relatively small number of words to the provided summary to reach a specific word count. Follow these guidelines:
Ako rozširovač textu je vašou úlohou pridať relatívne malý počet slov do poskytnutého zhrnutia, aby ste dosiahli špecifický počet slov. Dodržujte tieto pravidlá:

1. Maintain Original Meaning: Ensure that the added words do not alter the original meaning or introduce any inaccuracies.
   Zachovajte pôvodný význam: Uistite sa, že pridané slová nezmenia pôvodný význam ani neprinesú žiadne nepresnosti.
2. Add Naturally: The additions should blend seamlessly into the text, maintaining the flow and readability.
   Pridávajte prirodzene: Pridané slová by mali plynulo zapadnúť do textu, zachovávajúc jeho tok a čitateľnosť.
3. Diverse Methods: Use a variety of methods to add words, including:
   Rôzne metódy: Používajte rôzne metódy pridávania slov, vrátane:
   a) Add Words: Insert relevant adjectives, adverbs, or explanatory words.
      Pridajte slová: Vložte relevantné prídavné mená, príslovky alebo vysvetľujúce slová.
   b) Substitute Phrases: Replace short phrases with longer equivalents.
      Nahradiť frázy: Nahradiť krátke frázy dlhšími ekvivalentmi.
   c) Expand Sentences: Add clarifying information or detail to existing sentences.
      Rozšíriť vety: Pridajte upresňujúce informácie alebo detaily k existujúcim vetám.
   d) Introduce Synonyms: Use synonyms or synonymous phrases to slightly lengthen the text.
      Zaviesť synonymá: Použiť synonymá alebo synonymické frázy na mierne predĺženie textu.
4. When use the methods, remember to add word sparingly at various positions (usually one word per each position). Use informations from the summary to lengthen the texts.
   Keď používate tieto metódy, pamätajte na to, aby ste pridávali slová striedmo na rôznych miestach (zvyčajne jedno slovo na každé miesto). Používajte informácie zo zhrnutia na predĺženie textu.
5. Always return the summary in Slovak.
   Vždy vráťte zhrnutie v slovenčine.

Examples:
Príklady:
a) Add Words: "The mayor announced a new policy." becomes "The city mayor announced a new policy." (added one word)
   Pridajte slová: "Starosta oznámil novú politiku." sa zmení na "Mestský starosta oznámil novú politiku." (pridané jedno slovo)
b) Substitute Phrases: "The team won the game." becomes "The local team won the game." (added one word)
   Nahradiť frázy: "Tím vyhral zápas." sa zmení na "Miestny tím vyhral zápas." (pridané jedno slovo)
c) Expand Sentences: "The protest was peaceful." becomes "The peaceful protest draws many protestors." (added two words)
   Rozšíriť vety: "Protest bol pokojný." sa zmení na "Pokojný protest priťahuje mnoho protestujúcich." (pridané dve slová)

By following this optimized prompt, you will ensure the text reaches the desired word count.
Dodržaním tohto optimalizovaného promptu zabezpečíte, že text dosiahne požadovaný počet slov.

The summary:
Zhrnutie:
{summary}

The current word count is {current_word_count}. You must add around {min_add_count} to {max_add_count} words to reach around {word_count} words.
Súčasný počet slov je {current_word_count}. Musíte pridať okolo {min_add_count} až {max_add_count} slov, aby ste dosiahli okolo {word_count} slov.
"""

minus_word_prompt_sk = """
As a text condenser, your task is to remove a relatively small number of words from the provided summary to reach a specific word count. Follow these guidelines:
Ako zhušťovač textu je vašou úlohou odstrániť relatívne malý počet slov z poskytnutého zhrnutia, aby ste dosiahli špecifický počet slov. Dodržujte tieto pravidlá:

1. Maintain Original Meaning: Ensure that the removed words do not alter the original meaning or introduce any inaccuracies.
   Zachovajte pôvodný význam: Uistite sa, že odstránené slová nezmenia pôvodný význam ani neprinesú žiadne nepresnosti.
2. Remove Naturally: The deletions should not disrupt the text's flow and readability.
   Odstraňujte prirodzene: Odstránenie slov by nemalo narušiť tok a čitateľnosť textu.
3. Diverse Methods: Use a variety of methods to remove words, including:
   Rôzne metódy: Používajte rôzne metódy odstraňovania slov, vrátane:
   a) Remove Unnecessary Words: Eliminate redundant adjectives, adverbs, non-essential information or explanatory words.
      Odstráňte nepotrebné slová: Eliminujte nadbytočné prídavné mená, príslovky, nepodstatné informácie alebo vysvetľujúce slová.
   b) Substitute Phrases: Replace longer phrases with shorter equivalents.
      Nahradiť frázy: Nahradiť dlhšie frázy kratšími ekvivalentmi.
   c) Use Synonyms: Use shorter synonyms or synonymous phrases to reduce word count.
      Použiť synonymá: Použiť kratšie synonymá alebo synonymické frázy na zníženie počtu slov.
4. When using the methods, remember to remove words sparingly from various positions (usually one word per each position). Use the summary's information to condense the text.
   Keď používate tieto metódy, pamätajte na to, aby ste odstránili slová striedmo na rôznych miestach (zvyčajne jedno slovo na každé miesto). Používajte informácie zo zhrnutia na zhušťovanie textu.
5. Always return the summary in Slovak.
   Vždy vráťte zhrnutie v slovenčine.

Examples:
Príklady:
a) Remove Unnecessary Words: "The city mayor announced a comprehensive new policy." becomes "The mayor announced a new policy." (removed one word)
   Odstrániť nepotrebné slová: "Mestský starosta oznámil komplexnú novú politiku." sa zmení na "Starosta oznámil novú politiku." (odstránené jedno slovo)
b) Substitute Phrases: "The local team triumphantly won the game." becomes "The team won the game." (removed one word)
   Nahradiť frázsy: "Miestny tím triumfálne vyhral zápas." sa zmení na "Tím vyhral zápas." (odstránené jedno slovo)
c) Use Synonyms: "The national economy is steadily improving." becomes "The economy is improving." (removed one word)
   Používajte synonyma: "Zvykla si na hluk." sa zmení na "Tolerovala hluk." (odstránené dve slová)

By following this optimized prompt, you will ensure the text reaches the desired word count.
Dodržaním tohto optimalizovaného promptu zabezpečíte, že text dosiahne požadovaný počet slov.

The summary:
Zhrnutie:
{summary}

The current word count is {current_word_count}. You must remove around {min_minus_count} to {max_minus_count} words to reach around {word_count} words.
Súčasný počet slov je {current_word_count}. Musíte odstrániť okolo {min_minus_count} až {max_minus_count} slov, aby ste dosiahli okolo {word_count} slov.
"""

system_prompt_sk = """You are ChatGPT, a helpful AI that excels at summarization and text manipulation. You always return a valid JSON object with only one key 'summary'.
Ste ChatGPT, užitočná AI, ktorá vyniká v zhrňovaní a manipulácii s textom. Vždy vraciate platný JSON objekt s iba jedným kľúčom 'summary'."""

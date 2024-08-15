import gptzzzs

thing = gptzzzs.Gptzzzs()


text = "John F. Kennedy, who served as the 35th President of the United States from 1961 until his assassination in 1963, is widely considered as one of the best Presidents in American history. He was a charismatic leader who inspired and united the nation, particularly during the Civil Rights Movement. Kennedy's speeches, such as his inaugural address in which he famously said \"Ask not what your country can do for you, ask what you can do for your country,\" and his famous Moon speech in which he challenged the nation to put a man on the moon within a decade, are still remembered and quoted today. Additionally, Kennedy's foreign policy was marked by a strong commitment to peace and diplomacy, as exemplified by the Cuban Missile Crisis, where his cool and steady leadership helped to defuse a potentially catastrophic conflict with the Soviet Union. Overall, JFK's legacy as a visionary leader who inspired a generation and left a lasting impact on the world continues to make him one of the most beloved Presidents in American history."

response = thing.change_text(text, synonym_list="zaibacu", percent_synonyms=80)

print(response)
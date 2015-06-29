# Collections!
# Pronounce Dict, and each of them contains K = Pronounce, V = Chinese Words Set
# Pronounce Dict will be ouputted as [pronounce 2 chinese import].py
prSet = Dict()

# Chinese and its Pronounce will be just outputted as [chinese 2 pronounce import].py

# Opening target.csv IO
input = open("target.csv")

# Opening chinese_pronounce IO
chinese_pronounce = open("importChinseWordsToSqlite.py", "w")
println(chinese_pronounce, "from queryChinese.models import ChineseWord")

# Opening pronounce_set IO
pronounce_set = open("importPronouncesToSqlite.py", "w")
println(pronounce_set, "from queryClosePronounce.models import Pronounce")

# Every Line
for ln in eachline(input)
    #Chinese Tmp
    chTmp = split(ln, ",")[2]

    # Pronounce Tmp
    prTmp = split(ln, ",")[3]
    prTmp = replace(prTmp, " ", "-")
    prTmp = replace(prTmp, "--", "-")

    # Pronounce after cleaned the "--"
    prList = String[]

    # Cleaning pronounce by entering them
    for prTmpTmp in split(prTmp, "/")
        # For append later
        prToAppend = prTmpTmp

        # Look for the head is "-"
        if (prToAppend[1] == '-')
            prToAppend = prToAppend[2:end]
        end

        # Look for the last is "-"
        if (prToAppend[end] == '-')
            prToAppend = prToAppend[1:end-1]
        end

        # Append to prList
        push!(prList, prToAppend)
    end

    # Join them with "/"
    prResult = join(prList, "/")

    # Write to that file
    println(chinese_pronounce, "ChineseWord.objects.create(word='$(chTmp)', pronounce='$(prResult)')")

    # Wow part
    for prTmpTmp in split(prResult, "/")
        for (ch, pr) in zip(chTmp, split(prTmpTmp, "-"))
            if (haskey(prSet, lowercase(pr)))
                prSet[lowercase(pr)] = union(prSet[lowercase(pr)], [ch])
            else
                prSet[lowercase(pr)] = Set([ch])
            end
        end
    end

end

# Write Set to pronounce_set
for key in collect(keys(prSet))

    valueTmp = String[]

    for ch in prSet[key]
        push!(valueTmp, string(ch))
    end

    valueResult = join(valueTmp, ",")

    println(pronounce_set, "Pronounce.objects.create(pronounce='$(key)', chineses='$(valueResult)')")
end

# Closing ALL IO
close(input)
close(chinese_pronounce)
close(pronounce_set)

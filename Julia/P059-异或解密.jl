function main()
    code = 'a':'z'.|>Int
    txt = split(read("59_异或解密/p059_cipher.txt",String),",")
    word = parse.(Int,txt)
    f = open("p059_decipher.txt","w")
    good = similar(word)
    for keys in Iterators.product(code,code,code)
        for (id,key) in zip(eachindex(word),Iterators.cycle(keys))
            good[id] = xor(word[id],key)
        end
        write(f,join(Char.(good)),'\n')
    end
    close(f)

    for line in eachline("p059_decipher.txt")
        if line ⊆ ' ':'z'
            println(line,'\n')
        end
    end
end

@time main()

# 0.780185 seconds (159.85 k allocations: 179.385 MiB, 3.21% gc time)
# 0.792415 seconds (159.85 k allocations: 179.385 MiB, 1.59% gc time)

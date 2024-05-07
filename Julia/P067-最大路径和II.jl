# 花了一晚上把它秒杀了
# 0.197281 seconds (64.80 k allocations: 5.432 MiB, 92.17% compilation time)
# 7273
@time foldr((x, y) -> @.(x + max(y[1:end-1], y[2:end])), [vec(eval(Meta.parse("[$i]"))) for i in eachline("P067-最大路径和II.txt")]) |> only
function read_data(path::AbstractString)
    data = [eval(Meta.parse("[$line]")) for line in eachline(path)]
    reduce(hcat, data)', length(data[1])
end
matrix::Matrix{Int}, dim::Int = read_data("$(@__DIR__)/data_file/0083_matrix.txt")

function Djikstra(matrix, dim)
    node_dict = Dict((1, 1) => matrix[1, 1]) ## 用小的字典动态增减，查找加速
    node_set = Set() ## 记录遍历过的值
    current = (1, 1)

    ### 记录路径需要记录中间状态值
    total = sum(matrix) ## 一个很大的数 >= 矩阵元素和
    cord = Iterators.product([1:dim;], [1:dim;]) |> collect  ## 矩阵坐标
    recording_nodes = Dict(key => total for key in cord)
    previous_nodes = Dict(key => (dim, dim) for key in cord)

    while current != (dim, dim)
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]
            next = current .+ direction
            ### 坐标判断
            (next in node_set ||
             next[1] in [0, dim + 1] ||
             next[2] in [0, dim + 1]) && continue
            new_val = node_dict[current] + matrix[next...]
            ### 更新路径值
            node_dict[next] = next ∉ keys(node_dict) ?
                              new_val :
                              min(new_val, node_dict[next])
            ### 记录路径
            if new_val < recording_nodes[next]
                recording_nodes[next] = new_val
                previous_nodes[next] = current
            end
        end
        delete!(node_dict, current) ## 删掉不需要的node
        push!(node_set, current)
        current = findmin(values, node_dict) |> last
    end

    path_sum = node_dict[current]
    ### 得到经过的路径
    find_path = [(80, 80)]
    while current !== (1, 1)
        current = previous_nodes[current]
        push!(find_path, current)
    end

    return path_sum, find_path |> reverse!
end

@time path_sum, path = Djikstra(matrix, dim)
# 0.005449 seconds (45.72 k allocations: 4.331 MiB)
# 0.005469 seconds (45.72 k allocations: 4.331 MiB)
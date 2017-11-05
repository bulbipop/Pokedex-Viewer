delay = 1800                -- every 30 seconds
remains = delay

while true do
    remains = remains - 1
    if remains == 0 then
        local file = io.open("../pkdx_memory.txt", "w")
        pkdx = memory.readbyterange(0x12F6, 20)
        for k,v in ipairs(pkdx) do
            file:write(tostring(v), "\n")
        end
        file:close()

        local file = io.open("../pkmns_road.txt", "w")
        pkmns = memory.readbyterange(0x1886, 20)
        for k,v in ipairs(pkmns) do
            file:write(tostring(v), "\n")
        end
        file:close()
        remains = delay
    end
    emu.frameadvance()
end

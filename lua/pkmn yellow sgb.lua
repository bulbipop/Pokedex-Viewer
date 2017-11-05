delay = 1800                -- every 30 seconds
remains = delay

while true do
    remains = remains - 1
    if remains == 0 then
        local file = io.open("../pkdx_memory.txt", "w")
        pkdx = memory.readbyterange(0x12F5, 20)
        for k,v in ipairs(pkdx) do
            file:write(tostring(v), "\n")
        end
        remains = delay
        file:close()
    end
    emu.frameadvance()
end

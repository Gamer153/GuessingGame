local number = nil
local random = math.random(1000)
local tries = 0
while number ~= random do
    number = nil
    while number == nil do
        io.write("Guess a number between 0 and 1000: ")
        number = io.read("l")
        number = tonumber(number)
        if number == nil then
            print("Invalid number!")
        end
    end
    if number < random then
        print("Too small!")
    elseif number > random then
        print("Too big!")
    end
    tries = tries + 1
end
print("You guessed it in only " .. tries .. " tries! It was " .. random .. ".")


local shemat41 = function(marche) 
    for i = 1,5  do
        turtle.forward(marche)
        turtle.backward(marche//2)
        turtle.turnLeft(90)
    end
end

local goBottomToLeft = function(marche)
    turtle.turnRight(90)
    turtle.forward(marche//2)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end



local goLeftToTop = function(marche)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end


local goTopToRight = function(marche)

    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)

end



local goRightToBottom = function(marche)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end



shemat41(100)

for i=1,100 do
    choix = math.random(1, 4)

    if choix == 1 then
        goBottomToLeft(100)
    elseif choix == 2 then
        goBottomToLeft(100)
        goLeftToTop(100)
    elseif choix == 3 then
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
    elseif choix == 4 then
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
        goRightToBottom(100)
    end

end

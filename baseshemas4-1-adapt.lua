



local shemat41 = function(marche) 
    for i = 1,5  do
       for i=1,marche do
	turtle.forward()
end
       for i=1,math.floor(marche / 2) do
			turtle.back()
	    end
        turtle.turnLeft()

    end
end

local goBottomToLeft = function(marche)
    turtle.turnRight()
    for i=1,math.floor(marche / 2) do
	turtle.forward()
end
    for i=1,2 do
    	turtle.turnRight()
    end
    for i=1,2 do
    	turtle.turnRight()
    end
   for i=1,marche do
	turtle.forward()
end
    turtle.turnLeft()
    for i=1,math.floor(marche / 2) do
	turtle.forward()
end
end



local goLeftToTop = function(marche)
    for i=1,2 do
    	turtle.turnRight()
    end
   for i=1,marche do
	turtle.forward()
end
    turtle.turnLeft()
    for i=1,math.floor(marche / 2) do
	turtle.forward()
end
end


local goTopToRight = function(marche)

    for i=1,2 do
    	turtle.turnRight()
    end
   for i=1,marche do
	turtle.forward()
end
    turtle.turnLeft()
    for i=1,math.floor(marche / 2) do
	turtle.forward()
end

end



local goRightToBottom = function(marche)
    for i=1,2 do
    	turtle.turnRight()
    end
   for i=1,marche do
	turtle.forward()
end
    turtle.turnLeft()
    for i=1,math.floor(marche / 2) do
	turtle.forward()
end
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


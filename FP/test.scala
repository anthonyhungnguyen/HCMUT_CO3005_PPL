val inc = (x:Int) => x + 1

val dub = (x:Int) => 2 * x
val incdub = dub compose inc
println(incdub(3))
object MainObject {
    def main(args: Array[String]) = {
        println(squareListRec(5))
        // println(squareListHOF(5))
        // println(powRec(5,5))
        // println(powHOF(5,5))
        // println(appendRec(List(1,2,3),List(4,5,6)))
        // println(appendHOF(List(1,2,3),List(4,5,6)))
        // println(reverseRec(List(5,6,7)))
        // println(reverseHOF(List(5,6,7)))
        // println(lessThanRec(5,List(1,2,3,4,5,6,7)))
        // println(lessThanHOF(5,List(1,2,3,4,5,6,7)))
    }

    def squareListRec(n:Int): List[Int] = if (n <= 0) List() else squareListRec(n-1):::List(n*n)

    def squareListHOF(n:Int): List[Int] = {
        val lst = List.range(1,n+1)
        lst map (x => x * x)
    }
    def powRec(x:Double, n: Int):Double = {
        if (n>0) {
            powRec(x,n-1)*x
        } else if (n==0) {
            1
        } else {
            powRec(x,n+1)*1/x
        }
    }
    def powHOF(x:Double, n:Int):Double = {
        val lst = List.fill(n)(x)
        lst.reduce((x,y) => x*y)  
    }

    def appendRec(a:List[Int],b:List[Int]):List[Int] = b match {
        case Nil => a
        case h::t => appendRec(a:::List(h),t)
    }

    def appendHOF(a:List[Int],b:List[Int]):List[Int] = {
        a.foldRight(b)(_::_)
    }

    def reverseRec(a:List[Int]):List[Int] = a match {
        case Nil => Nil
        case h::t => reverseRec(t):::List(h)
    }
    def reverseHOF(a:List[Int]):List[Int] = {
        a.foldLeft(List[Int]())((x,y) => y::x)
    }
    def lessThanRec(n:Int, lst: List[Int]):List[Int] = {
        if (lst != Nil) {
            if (lst.head < n) {
                lst.head::lessThanRec(n,lst.tail)
            } else {
                Nil
            }
        } else {
            Nil
        }
    }
    def lessThanHOF(n:Int, lst: List[Int]):List[Int] = {
        lst.filter(_<n)
    }
}
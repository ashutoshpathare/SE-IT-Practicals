import java.util.*;
class Complex_Op
{
        float real, imag;
        Complex_Op()
         {
            real=0;
            imag=0;
         }
    Complex_Op(float Comp1, float Comp2)
        {
            real=Comp1;
            imag=Comp2;
        }
    void AddNum(Complex_Op C1, Complex_Op C2)
        {
            float real, imag;
            real = (C1.real+C2.real);
            imag = (C1.imag+C2.imag);
            System.out.println("Addition:="+real+"+"+imag+"i");
        }
    void SubNum(Complex_Op C1, Complex_Op C2)
        {
            float real, imag;
            real = (C1.real-C2.real);
            imag = (C1.imag-C2.imag);
            System.out.println("Subtraction:="+real+"+"+imag+"i"); 
        }
    void MulNum(Complex_Op C1, Complex_Op C2)
        {
            float real, imag;
            real = (C1.real*C2.real-C1.imag*C2.imag);
            imag = (C1.real*C2.imag-C2.real*C1.imag);
            System.out.println("Multiplication:="+real+"+"+imag+"i"); 
        }
    void DivNum(Complex_Op C1, Complex_Op C2)
        {
            float real, imag, deno;
            deno = (C2.real*C2.real+C2.imag*C2.imag);
            real = (C1.real*C2.real+C1.imag*C2.imag)/deno;
            imag = (C2.real*C1.imag-C1.real*C2.imag)/deno;
            System.out.println("Division:="+real+"+"+imag+"i");
        }
}

public class Complex
 {
    public static void main(String[] args){
        int num1, num2, answer;
        Complex_Op cal = new Complex_Op();
        Scanner input = new Scanner(System.in);

        System.out.println("Enter first number");
        num1=input.nextInt();
        num2=input.nextInt();
        Complex_Op Object1 = new Complex_Op(num1, num2);
        
        System.out.println("Enter second Number");
        num1=input.nextInt();
        num2=input.nextInt();
        Complex_Op Object2 = new Complex_Op(num1, num2);

        cal.AddNum(Object1, Object2);
        cal.SubNum(Object1, Object2);
        cal.MulNum(Object1, Object2);
        cal.DivNum(Object1, Object2);
    }
 }

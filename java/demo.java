import java.util.List;
import java.util.ArrayList;
//import org.slf4j.Logger;
import java.util.logging.*;
class hello{
	public static Logger log = Logger.getLogger("hello");
	public static void main(String[] args){
		System.out.println(args+"\r" + "hello world!");
		name huang = RT("huang_jian");//new t("huang_jian");//new name("huang_jian");
		huang.getname();
		t qyy = new t("qyy");
		System.out.println(qyy.getname());
		System.out.println(huang);
		//System.out.println(() -> new dex());
		List<name> list = new ArrayList<name>();
		System.out.println(new one.two("huang l q").get());
		log.info("hello minecraft mod dev");
	}

	public static name RT(String argss){
		return new name(argss);
	}
}


class one{
	static class two{
		private static String name;
		two(String name){
			two.name = name;
		}
		static String get(){
			return two.name;
		}
	}
}





class dex{
	public String dex(){
		return "qyy";
	}
}


class mod{
	String name;
	public mod(String name){
		this.name = name;
	}
	public void imp(String xde){
		System.out.println(xde);
	}
}

class name{
	String name;
	public name(String name){
		this.name = name;
	}
	String getname(){
		System.out.println(this.name);
		return this.name;
	}
}

class t extends name{
	public t(String n){
		super(n);
		super.getname();
	}
}
/*
@mod("huang_jian")
class xdes{
	public xdes(){

	}
}*/
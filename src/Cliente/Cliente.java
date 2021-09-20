/**
 * 
 */
package Cliente;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

/**
 * @author S2G11
 *
 */
public class Cliente {

	public static void main(String[] args) {
		int PUERTO = 5000;
		
		try (Socket socket = new Socket("localhost", PUERTO)){
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			
			BufferedReader in = new BufferedReader(new java.io.InputStreamReader(socket.getInputStream()));
			
			Scanner sc = new Scanner(System.in);
			String mensaje = null;
			
			while(!"exit".equalsIgnoreCase(mensaje)) {
				mensaje = sc.next();
				
				out.println(mensaje);
				out.flush();
				
				System.out.println("El servidor responde:" + in.readLine());
			}
			
			sc.close();
			
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

}

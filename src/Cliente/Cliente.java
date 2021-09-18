/**
 * 
 */
package Cliente;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * @author S2G11
 *
 */
public class Cliente {

	
	
	
	//----------------------------------------
	// MAIN
	//----------------------------------------
	public static void main(String[] args) {
		
		final String HOST= "127.0.0.1";
		final int PUERTO = 5000;
		DataInputStream in;
		DataOutputStream out;
		
		try {
			Socket sc = new Socket(HOST, PUERTO);
			in = new DataInputStream(sc.getInputStream());
			out = new DataOutputStream(sc.getOutputStream());
			
			out.writeUTF("Cliente");
			
			String mensaje = in.readUTF();
			
			System.out.println(mensaje);
			
			sc.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}

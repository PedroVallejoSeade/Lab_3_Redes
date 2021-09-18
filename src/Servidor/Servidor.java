/**
 * 
 */
package Servidor;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author S2G11
 *
 */
public class Servidor {

	
	
	
	//----------------------------------------
	// MAIN
	//----------------------------------------
	public static void main(String[] args) {
		ServerSocket servidor = null;
		Socket sc = null;
		DataInputStream in;
		DataOutputStream out;
		final int PUERTO = 5000;
		
		try {
			servidor = new ServerSocket(PUERTO);
			System.out.println("Servidor iniciado");
			while (true) {
				sc = servidor.accept();
				
				in = new DataInputStream(sc.getInputStream());
				out = new DataOutputStream(sc.getOutputStream());
				
				String mensaje = in.readUTF();
				System.out.println(mensaje);
				
				out.writeUTF("Servidor");
				
				sc.close();
				System.out.println("Cliente desconectado");
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}

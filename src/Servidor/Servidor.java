/**
 * 
 */
package Servidor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author S2G11
 *
 */
public class Servidor {

	public static void main(String[] args) {
		ServerSocket servidor = null;
		int PUERTO = 5000;
		int numConexiones = 25;
		
		try {
			servidor = new ServerSocket(PUERTO, numConexiones);
			servidor.setReuseAddress(true);
			
			while(true) {
				Socket cliente = servidor.accept();
				
				System.out.println("Nuevo cliente conectado" + cliente.getInetAddress().getHostAddress());
				
				ManejadorClientes socketCliente = new ManejadorClientes(cliente);
				
				new Thread(socketCliente).start();
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if(servidor != null) {
				try {
					servidor.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	private static class ManejadorClientes implements Runnable {
		private final Socket socketCliente;
		
		public ManejadorClientes(Socket socket){
			this.socketCliente = socket;
		}
		
		public void run() {
			PrintWriter out = null;
			BufferedReader in = null;
			
			try {
				out = new PrintWriter(socketCliente.getOutputStream(), true);
				in = new BufferedReader(new InputStreamReader(socketCliente.getInputStream()));
				
				String mensajeCliente;
				while((mensajeCliente = in.readLine()) != null) {
					System.out.println("Mensaje del cliente: " + mensajeCliente);
					out.println("El mensaje \"" + mensajeCliente +"\" fue recibido por el servidor");
				}
			} catch(IOException e) {
				e.printStackTrace();
			} finally {
				try {
					if (out != null) {
						out.close();
					}
					if(in != null) {
						in.close();
						socketCliente.close();
					}
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
		}
	}

}

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import { Car, Wrench, History } from "lucide-react";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-neutral-900 text-neutral-100 flex flex-col">
      {/* Navbar */}
      <nav className="bg-neutral-950 text-blue-400 shadow-lg p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold">Fleet Manager</h1>
        <div className="space-x-4">
          <Button variant="ghost" className="text-blue-400 hover:text-blue-300">Accueil</Button>
          <Button variant="ghost" className="text-blue-400 hover:text-blue-300">Véhicules</Button>
          <Button variant="ghost" className="text-blue-400 hover:text-blue-300">Entretiens</Button>
        </div>
      </nav>

      {/* Content */}
      <main className="flex-1 container mx-auto p-6 space-y-10">
        {/* Section véhicules */}
        <section>
          <h2 className="text-xl font-semibold mb-4 text-blue-400 flex items-center gap-2"><Car /> Véhicules</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {Array.from({ length: 10 }).map((_, i) => (
              <motion.div key={i} whileHover={{ scale: 1.05 }}>
                <Card className="bg-neutral-800 border border-neutral-700">
                  <CardHeader>
                    <CardTitle className="text-blue-300">Véhicule {i + 1}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-neutral-400">Marque / Modèle</p>
                    <p className="text-neutral-500">Année / Kilométrage</p>
                    <Button className="mt-4 bg-blue-500 hover:bg-blue-600 text-white w-full">Détails</Button>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </section>

        {/* Section entretiens à prévoir */}
        <section>
          <h2 className="text-xl font-semibold mb-4 text-blue-400 flex items-center gap-2"><Wrench /> Entretiens à prévoir</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { vehicule: "Véhicule 1", entretien: "Vidange" },
              { vehicule: "Véhicule 3", entretien: "Pneus" },
              { vehicule: "Véhicule 7", entretien: "Freins" },
            ].map((item, i) => (
              <Card key={i} className="bg-neutral-800 border border-neutral-700">
                <CardHeader>
                  <CardTitle className="text-blue-300">{item.vehicule}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-neutral-400">{item.entretien}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Section derniers entretiens */}
        <section>
          <h2 className="text-xl font-semibold mb-4 text-blue-400 flex items-center gap-2"><History /> Derniers entretiens</h2>
          <div className="space-y-4">
            {[
              { vehicule: "Véhicule 2", details: ["Vidange - Jan 2025", "Freins - Déc 2024", "Pneus - Nov 2024"] },
              { vehicule: "Véhicule 5", details: ["Contrôle technique - Fév 2025", "Batterie - Jan 2025", "Carrosserie - Déc 2024"] },
            ].map((item, i) => (
              <Card key={i} className="bg-neutral-800 border border-neutral-700">
                <CardHeader>
                  <CardTitle className="text-blue-300">{item.vehicule}</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="list-disc list-inside text-neutral-400">
                    {item.details.map((d, j) => (
                      <li key={j}>{d}</li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-neutral-950 text-neutral-400 p-6 text-center">
        <p>© 2025 Fleet Manager. Tous droits réservés.</p>
      </footer>
    </div>
  );
}

import scrapy
import csv

class napa(scrapy.Spider):
    name = "napa"
    start_urls = []

    def __init__(self):
        writer = ["AS7051","AE727","AE771","AE7255M","AS773","AS783","AE7254M","AE754","MS7021","AE7013AM","AE728AM","MS792","AS791","AS7001","MS7009","AE7017M","AE7019M",
        "AE7027AM","MS7032","MS7039","MS7044","MAS795B","AS7048","AE7054M","AE7061AM","AE7185","MS7066","AS7064","MS7065","AE7067","AS7068","MS7069","MC7111","AE7046","MS7079",
        "AS7080","AE7024A","AE7082AM","AS7083A","AE7072AM","AE7084AM","AE7070AM","AE7045C","S7087","AE7070B","AS7089","AE7090","AE7091","MS7093","MS7096","AE7097A",
        "AE7099M","MS7101","AS7102","MS7103","AE7104","AS7105","AE7107","AE7108M","AE7110","AE7112","AE7113","AS7117","AS7118","AE7120","MAS7082C","AE7082B","AS7123",
        "AE7122A","AE7125AM","AE7127M","AE7135M","AE7136M","AE7133BM","AE7134AM","AE7139AM","MAS7140","AE7141M","AE7142M","AE7143","AE7144","MS7145","AE7146","AS7146",
        "AE7251M","AE7149M","AE7129","AE7153M","AE7154","TS795BM","AE7128M","AS7150","AE7156","AE7160","AE7161M","AE7162M","AE7106CM","AE7164AM","AE7165M","AE7166M",
        "AE7167M","AE7169","AE7171M","AE7174M","AE7146C","AE7178M","AE7110CM","AE7155M","AE7156B","AE7180","AE7181M","AE7182","AE7183","AE7104BM","AE7184M","AE7186","AE7188",
        "S7191","AE7192M","AE7572M","AE7193","AE7195M","AE7196M","AE7198M","AS7201","MS7202","MAS7203","AE7204","AE7205","AE7207","AE7208","AE7212","AE7212","AE7072BM",
        "AE7213","AE7215","AE7216M","AE7217M","AE7169AM","AE7219M","AE7220M","AE7221M","AE7146D","AE7222AM","AE7223","AE7224M","AE7175M","AE7225","S7226","AE7227M","AE7186A",
        "AE7228M","AE7229M","AE7230","AE7231A","AE7206","AE7232","AE7234","AE7236","AE7237EM","AE7238","AE7239A","AE7240M","AE7241","AE7242M","AE7244","AE7245","AE7247",
        "AE7248M","AE7249M","AE7250AM","AE788AM","TS7218","AE7253","AE7233","AE7256AE7418A","AE7257","AE7259M","AE7259BM","AE7263M","AE7233A","AE788AM","AE7265M","AE7266M",
        "AE7267M","MAS7271","AE7272","AE7274AM","AE7275AM","AE7246","AE7276M","AE7279","AE7281M","AE7284","AE7285M","AS7286","AE7203M","AE7287","AE7288","AE7289","AE7290M",
        "AE7291M","AE7494M","AE7293","AS7295","AE7296M","AE7297M","AE7235M","AE7298","AE7299M","AE7300M","AE7301M","AE7303M","AE7258CM","AE7304A","AE7305M","AE7252","AE7197M",
        "AE7308CM","AE7307M","AE7311M","MS7312","AE7317M","AE7146E","AE7318AM","AS7320","AE7321M","AE7298A","AE7322","AE7205A","AE7293AM","AE7326","AE7327","AE7329AM",
        "AE7054M","AE7331M","S7334","AE7336M","AE7337","AE7338","AE7260M","AE7340M","AE7341M","AE7345","AE7219AM","AE7348","AE7350M","AE7351M","AE7353M","AE7356M","AE7357",
        "AE7358A","AE7359AM","AE7360M","AE7362","AE7363M","AE7365","AE7342AM","AE7366M","MAS7368","AE7369M","AE7371","AE7278M","AE7437M","AE7374M","AS7375","AE7377M","AE7082C",
        "AE7380M","AE7381","AE7298BM","AE7382","AE7383","AE7384M","AE7385M","AE7386M","AE7387BM","AE7388M","AE7389M","AE7390","AE7393","AE7567M","AE7398M","AE7400M","AE7401M",
        "AE7403AM","AE7404AM","AE7337AM","AE7408M","AE7410M","AE7412","AE7413","AE7414","AE7416","AE7418","AE7419M","AE7421","AE7423M","AE7424A","AE7426","AE7428","AE7429M",
        "AE7430","AE7431","AE7277","AE7434AM","AE7435M","AE7436M","AE7437M","AE7440M","AE7441","AE7442","AE7446M","AE7447","AE7448","AE7451","AE7452","AE7456","AE7457","AE7458",
        "AE7459","AE7460","AE7461M","AE7462M","AE7463","AE7464","AE7467","AE7468","AE7469M","AE7470AM","AE7471M","AE7421A","AE7474","AE7476","AE7477A","AE7478M","AE7479M","AE7417",
        "AE7484","AE7485","AE7487M","AE7489A","AE7298C","AE7490","AE7491","AE7506M","AE7493","AE7495","AE7496M","AE7497","AE7384AM","AE7502AM","AE7504","AE7505M","AE7508M",
        "AE7509M","AE7510","AE7503M","AE7511AM","AE7512M","AE7513","AE7514","AE7515","AE7516M","AE7517M","AE7438B","AE7518AM","AE7520","AE7522M","AE7523M","AE7340AM","AE7528M",
        "AE7529M","AE7530AM","AE7531M","AE7532M","AE7535M","AE7438C","AE7537M","AE7540M","AE7541","AE7542M","AE7514","AE7543M","SS7544M","AE7502BM","AE7545AM","AE7546",
        "AE7547","AE7550M","PGD672C","AE7385M","AE7555","AE7556M","AE7557","AE7558MCMX7558","AE7559","AE77560M","AE7561M","AE7427M","AE7434AM","CMX7563","AE7566","AE7569M",
        "AE7387A","AE7574","AE7576M","AE7577M","AE7578M","AE7681M","AE7581","AE7582M","AE7583M","AE7584M","AE7587","AE7387BM","AE7588M","AE7589","AE7590","AE7591","AE7592M",
        "AE7593","AE7594","AE7596","AE7597M","AE7599M","AE7600M","AE7602M","AE7607M","AE7608M","AE7609M","AE7611","AE7616M","AE7617M","AE7618M","AE7619","AE7424BM","SS7621M",
        "AE7622","AE7626M","AE7627M","AE7438DM","AE7628M","AE7629M","AE7630M","AE7631M","AE7635M","AE7636M","AE7637M","AE7638","AE7639","AE7640","AE7641M","TS7642M","AE7644M",
        "AE7649M","AE7651M","AE7652M","AE7653M","AE7655M","AE-7656","AE7660M","AE7661M","AE7662M","AE7663","AE7664M","AE7665M","AE7666M","AE7667M","AE7670","AE7671M","AE7605M",
        "AE7672M","AE7673M","AE7674M","AE7675M","AE7676M","AE7679","AE7681M","AE7687M","AE7688","AE7690M","AE7691","AE7616AM","AE7694M","AE-7692","AE7696","AE7625M",
        "SD7697M","SD7699M","AE7701","AE7702","AE7703M","AE7704","AE7705","AE7706M","AE7707M","AE7708","AE7712M","AE7713M","AE7651M","AE7716M","AE7719M","AE7720M",
        "AE7723M","AE7566A","AE7732M","AE7733M","AE7734M","AE7694M","AE7738","AE7688","AE7739","AE7740","CMX7741","AE7743","AE7744M","AE7745","AE7746","AE7753M",
        "AE7580M","AE7758M","AE7759M","AE7760M","AE7761M","AE7762","AE7763M","CMX7766","AE7767M","AE7513","AE7769M","AE7771","AE7670","AE7775M","AE7776M","AE7777M",
        "AE7779M","AE7782M","AE7784M","CMX7785","CMX7787","AE7788M","AE7725AM","CMX7795","AE7822M","AE7823M","CMX7824","AE7825M","AE7826","AE7827M","AE7970M",
        "CMX7830","CMX7833","AE7834M","AE7835M","AE7837M","AE7838M","AE7839M","CMX7843","CMX7844","AE7846M","AE-7848-M","AE-7849-M","AE-7850-M","AE-7851-M",
        "CMX-7852","CMX-7853","CMX-7854","CMX-7855","CMX-7856","AE7858M","AE-7859-M","AE-7861-M","AE-7862-M","CMX78963","AE-7864-M","AE-7866-M","AE-7867-M",
        "CMX-7870","AE-7871-M","AE-7874-M","AE-7875-M","CMX7877","CMX-7883","AE-7890-M","CMX-7891","CMX7895","CMX-7897","CMX-7898","BD998","AE7901M","CMX7904",
        "CMX7905","CMX7906","AE7909M","CMX7913","AE7915M","AE7916M","CMX7918","CMX7922","CMX7924","CMX7926","CMX7927","CMX7932","CMX7937","AEC7939","CMX7940",
        "CMX7941","CMX7943","CMX7945","CMX7946","AE7947","AE7948M","AE7949M","CMX7950","AE7951","AE7952M","AE7953M","AEC7955","CMX7961","CMX7692","CMX7963",
        "CMX7965","AE7973M","AE7973AM","AE7974M","CMX7975","AEC7976","CMX7978","CMX7985","CMX7986","CMX7987","AE7915M","AE7991M","AE7992M","AEC7945","SD7997M",
        "AE7758M"]
        for x in writer:
            self.start_urls.append("https://www.napaonline.com/en/search?text=" + x)
    def parse(self, response):
        for model in response.css('div.listing-item'):
            yield{
                'modelNumber' : model.css( 'div.listing-detail-text.listing-detail-text-part::text').extract_first(),
                'name' : model.css('a.listing-item-title::text').extract_first(),
                'price' : model.css('span.listing-price-value::text').extract_first(),
            }
            #productListItemADOAD7822_203472555 > div.listing-content > div.listing-detail > div.listing-detail-item.listing-detail-item-part > div.listing-detail-text.listing-detail-text-par
            #productListItemADOAD7822_203472555 > div.listing-aside > div.listing-price-wrap > div.listing-price-block > div.listing-price > div.listing-price-amount > span.listing-price-value
            #productTitle
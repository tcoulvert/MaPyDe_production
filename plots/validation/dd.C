void dd()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Apr  7 12:40:11 2022) by ROOT version 6.18/02
   TCanvas *c = new TCanvas("c", "c",0,0,800,800);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c->SetHighLightColor(2);
   c->Range(-3.2,-4.634146,4.3,0.2439024);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetLogx();
   c->SetLogy();
   c->SetTickx(1);
   c->SetTicky(1);
   c->SetLeftMargin(0.16);
   c->SetRightMargin(0.04);
   c->SetTopMargin(0.05);
   c->SetBottomMargin(0.13);
   c->SetFrameFillStyle(0);
   c->SetFrameBorderMode(0);
   c->SetFrameFillStyle(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx15[26] = {
   0.005623413,
   0.01,
   0.01778279,
   0.03162278,
   0.05623413,
   0.1,
   0.1778279,
   0.3162278,
   0.5623413,
   1,
   1.778279,
   3.162278,
   5.623413,
   10,
   17.78279,
   31.62278,
   56.23413,
   100,
   177.8279,
   316.2278,
   562.3413,
   1000,
   1778.279,
   3162.278,
   5623.413,
   10000};
   Double_t Graph0_fy15[26] = {
   30.09331,
   1.232985,
   0.1006838,
   0.01790857,
   0.006138438,
   0.003265214,
   0.002386307,
   0.002272655,
   0.002671974,
   0.003656954,
   0.005538171,
   0.008944367,
   0.01503043,
   0.0258676,
   0.04514683,
   0.07943502,
   0.1404115,
   0.248846,
   0.4416737,
   0.7845757,
   1.394352,
   2.478703,
   4.406984,
   7.836006,
   13.93377,
   24.77729};
   TGraph *graph = new TGraph(26,Graph0_fx15,Graph0_fy15);
   graph->SetName("Graph0");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineColor(8);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph015 = new TH1F("Graph_Graph015","Graph",100,0.01,10000);
   Graph_Graph015->SetMinimum(0.0001);
   Graph_Graph015->SetMaximum(1);
   Graph_Graph015->SetDirectory(0);
   Graph_Graph015->SetStats(0);
   Graph_Graph015->SetLineStyle(0);
   Graph_Graph015->SetLineWidth(2);
   Graph_Graph015->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph015->GetXaxis()->SetLabelFont(42);
   Graph_Graph015->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph015->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph015->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph015->GetXaxis()->SetTitleOffset(1);
   Graph_Graph015->GetXaxis()->SetTitleFont(42);
   Graph_Graph015->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph015->GetYaxis()->SetLabelFont(42);
   Graph_Graph015->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph015->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph015->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph015->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph015->GetYaxis()->SetTitleFont(42);
   Graph_Graph015->GetZaxis()->SetLabelFont(42);
   Graph_Graph015->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph015->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph015->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph015->GetZaxis()->SetTitleOffset(1);
   Graph_Graph015->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph015);
   
   graph->Draw("la");
   
   Double_t Graph1_fx16[25] = {
   0.01,
   0.02,
   0.03,
   0.04,
   0.05,
   0.06,
   0.125,
   0.2,
   0.3,
   0.5,
   0.6,
   0.7,
   0.8,
   1,
   2,
   7,
   8,
   10,
   100,
   200,
   300,
   2000,
   3000,
   5000,
   10000};
   Double_t Graph1_fy16[25] = {
   1.028191,
   0.04969132,
   0.01473157,
   0.008754429,
   0.005998619,
   0.004605287,
   0.00282145,
   0.002342371,
   0.002167374,
   0.002307424,
   0.002503183,
   0.002707903,
   0.00296043,
   0.003458439,
   0.006599727,
   0.01956045,
   0.0229569,
   0.02720616,
   0.2368412,
   0.4861305,
   0.7191982,
   4.851313,
   7.250552,
   11.976,
   24.39009};
   graph = new TGraph(25,Graph1_fx16,Graph1_fy16);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");
   graph->SetLineColor(8);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph116 = new TH1F("Graph_Graph116","Graph",100,0.009,11000);
   Graph_Graph116->SetMinimum(0.001950636);
   Graph_Graph116->SetMaximum(26.82889);
   Graph_Graph116->SetDirectory(0);
   Graph_Graph116->SetStats(0);
   Graph_Graph116->SetLineStyle(0);
   Graph_Graph116->SetLineWidth(2);
   Graph_Graph116->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph116->GetXaxis()->SetLabelFont(42);
   Graph_Graph116->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph116->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph116->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph116->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph116->GetXaxis()->SetTitleFont(42);
   Graph_Graph116->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph116->GetYaxis()->SetLabelFont(42);
   Graph_Graph116->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph116->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph116->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph116->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph116->GetYaxis()->SetTitleFont(42);
   Graph_Graph116->GetZaxis()->SetLabelFont(42);
   Graph_Graph116->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph116->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph116->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph116->GetZaxis()->SetTitleOffset(1);
   Graph_Graph116->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph116);
   
   graph->Draw("l");
   
   Double_t Graph2_fx17[25] = {
   0.01,
   0.01778279,
   0.03162278,
   0.05623413,
   0.1,
   0.1778279,
   0.3162278,
   0.5623413,
   1,
   1.778279,
   3.162278,
   5.623413,
   10,
   17.78279,
   31.62278,
   56.23413,
   100,
   177.8279,
   316.2278,
   562.3413,
   1000,
   1778.279,
   3162.278,
   5623.413,
   10000};
   Double_t Graph2_fy17[25] = {
   116.1218,
   3.508011,
   0.2665976,
   0.03573005,
   0.009067233,
   0.003888913,
   0.002474041,
   0.002151295,
   0.002384539,
   0.003142789,
   0.004644189,
   0.007381366,
   0.01227831,
   0.02099984,
   0.0365156,
   0.06411022,
   0.1131829,
   0.2004487,
   0.3556323,
   0.6315924,
   1.122327,
   1.994989,
   3.546828,
   6.306429,
   11.21377};
   graph = new TGraph(25,Graph2_fx17,Graph2_fy17);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph217 = new TH1F("Graph_Graph217","Graph",100,0.01,10000);
   Graph_Graph217->SetMinimum(0.0001);
   Graph_Graph217->SetMaximum(1);
   Graph_Graph217->SetDirectory(0);
   Graph_Graph217->SetStats(0);
   Graph_Graph217->SetLineStyle(0);
   Graph_Graph217->SetLineWidth(2);
   Graph_Graph217->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph217->GetXaxis()->SetLabelFont(42);
   Graph_Graph217->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph217->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph217->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph217->GetXaxis()->SetTitleOffset(1);
   Graph_Graph217->GetXaxis()->SetTitleFont(42);
   Graph_Graph217->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph217->GetYaxis()->SetLabelFont(42);
   Graph_Graph217->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph217->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph217->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph217->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph217->GetYaxis()->SetTitleFont(42);
   Graph_Graph217->GetZaxis()->SetLabelFont(42);
   Graph_Graph217->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph217->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph217->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph217->GetZaxis()->SetTitleOffset(1);
   Graph_Graph217->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph217);
   
   graph->Draw("l");
   
   Double_t Graph3_fx18[26] = {
   0.02,
   0.03,
   0.04,
   0.05,
   0.06,
   0.1,
   0.125,
   0.2,
   0.5,
   0.6,
   0.8,
   1,
   2,
   3,
   5,
   8,
   10,
   20,
   30,
   100,
   200,
   300,
   2000,
   3000,
   5000,
   10000};
   Double_t Graph3_fy18[26] = {
   1.746905,
   0.2102729,
   0.07106438,
   0.03406065,
   0.01976758,
   0.0068277,
   0.005335598,
   0.003212047,
   0.001946524,
   0.001891705,
   0.001914681,
   0.002060456,
   0.003150791,
   0.004142449,
   0.006247667,
   0.009096727,
   0.01066191,
   0.02370967,
   0.03419182,
   0.1064492,
   0.2047466,
   0.3056498,
   2.021656,
   3.017428,
   5.059793,
   10.04815};
   graph = new TGraph(26,Graph3_fx18,Graph3_fy18);
   graph->SetName("Graph3");
   graph->SetTitle("Graph");
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph318 = new TH1F("Graph_Graph318","Graph",100,0.018,11000);
   Graph_Graph318->SetMinimum(0.001702535);
   Graph_Graph318->SetMaximum(11.05277);
   Graph_Graph318->SetDirectory(0);
   Graph_Graph318->SetStats(0);
   Graph_Graph318->SetLineStyle(0);
   Graph_Graph318->SetLineWidth(2);
   Graph_Graph318->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph318->GetXaxis()->SetLabelFont(42);
   Graph_Graph318->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph318->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph318->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph318->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph318->GetXaxis()->SetTitleFont(42);
   Graph_Graph318->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph318->GetYaxis()->SetLabelFont(42);
   Graph_Graph318->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph318->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph318->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph318->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph318->GetYaxis()->SetTitleFont(42);
   Graph_Graph318->GetZaxis()->SetLabelFont(42);
   Graph_Graph318->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph318->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph318->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph318->GetZaxis()->SetTitleOffset(1);
   Graph_Graph318->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph318);
   
   graph->Draw("l");
   
   TLegend *leg = new TLegend(0.6,0.16,0.95,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetTextSize(0.03);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph0","m_{S} = 7 GeV","L");
   entry->SetLineColor(8);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph2","m_{S} = 15 GeV","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   
   leg = new TLegend(0.2,0.16,0.45,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetTextSize(0.032);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   entry=leg->AddEntry("Graph3","CMS result","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph2","this work","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}

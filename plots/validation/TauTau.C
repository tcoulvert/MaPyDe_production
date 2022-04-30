void TauTau()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Apr  7 12:39:30 2022) by ROOT version 6.18/02
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
   
   Double_t Graph0_fx11[26] = {
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
   Double_t Graph0_fy11[26] = {
   39.83747,
   1.044312,
   0.08936608,
   0.01854413,
   0.006750401,
   0.003796743,
   0.002978452,
   0.003031166,
   0.003751148,
   0.005312295,
   0.008219858,
   0.01345346,
   0.02279087,
   0.03941043,
   0.06897222,
   0.1215453,
   0.2150369,
   0.3812923,
   0.6769415,
   1.202689,
   2.137614,
   3.800174,
   6.756669,
   12.01414,
   21.3634,
   37.98899};
   TGraph *graph = new TGraph(26,Graph0_fx11,Graph0_fy11);
   graph->SetName("Graph0");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineColor(8);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph011 = new TH1F("Graph_Graph011","Graph",100,0.01,10000);
   Graph_Graph011->SetMinimum(0.0001);
   Graph_Graph011->SetMaximum(1);
   Graph_Graph011->SetDirectory(0);
   Graph_Graph011->SetStats(0);
   Graph_Graph011->SetLineStyle(0);
   Graph_Graph011->SetLineWidth(2);
   Graph_Graph011->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph011->GetXaxis()->SetLabelFont(42);
   Graph_Graph011->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph011->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph011->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph011->GetXaxis()->SetTitleOffset(1);
   Graph_Graph011->GetXaxis()->SetTitleFont(42);
   Graph_Graph011->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph011->GetYaxis()->SetLabelFont(42);
   Graph_Graph011->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph011->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph011->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph011->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph011->GetYaxis()->SetTitleFont(42);
   Graph_Graph011->GetZaxis()->SetLabelFont(42);
   Graph_Graph011->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph011->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph011->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph011->GetZaxis()->SetTitleOffset(1);
   Graph_Graph011->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph011);
   
   graph->Draw("la");
   
   Double_t Graph1_fx12[24] = {
   0.01,
   0.02,
   0.03,
   0.04,
   0.05,
   0.1,
   0.3,
   0.5,
   0.6,
   0.7,
   1,
   3,
   4,
   5,
   6,
   8,
   20,
   30,
   100,
   200,
   300,
   2000,
   3000,
   5000};
   Double_t Graph1_fy12[24] = {
   1.550055,
   0.07017527,
   0.02100046,
   0.01133625,
   0.007370654,
   0.003611435,
   0.003115478,
   0.003616478,
   0.003900742,
   0.004167641,
   0.005125481,
   0.01578349,
   0.02068422,
   0.02486452,
   0.02908478,
   0.03748002,
   0.08569175,
   0.1276043,
   0.4898161,
   0.9858403,
   1.475275,
   9.862888,
   14.70588,
   24.90323};
   graph = new TGraph(24,Graph1_fx12,Graph1_fy12);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");
   graph->SetLineColor(8);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph112 = new TH1F("Graph_Graph112","Graph",100,0.009,5499.999);
   Graph_Graph112->SetMinimum(0.00280393);
   Graph_Graph112->SetMaximum(27.39325);
   Graph_Graph112->SetDirectory(0);
   Graph_Graph112->SetStats(0);
   Graph_Graph112->SetLineStyle(0);
   Graph_Graph112->SetLineWidth(2);
   Graph_Graph112->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph112->GetXaxis()->SetLabelFont(42);
   Graph_Graph112->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph112->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph112->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph112->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph112->GetXaxis()->SetTitleFont(42);
   Graph_Graph112->GetYaxis()->SetTitle("95% CL upper limit on B(H ightarrow SS)");
   Graph_Graph112->GetYaxis()->SetLabelFont(42);
   Graph_Graph112->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph112->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph112->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph112->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph112->GetYaxis()->SetTitleFont(42);
   Graph_Graph112->GetZaxis()->SetLabelFont(42);
   Graph_Graph112->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph112->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph112->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph112->GetZaxis()->SetTitleOffset(1);
   Graph_Graph112->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph112);
   
   graph->Draw("l");
   
   Double_t Graph2_fx13[25] = {
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
   Double_t Graph2_fy13[25] = {
   168.2561,
   2.709898,
   0.2303411,
   0.03957108,
   0.01102901,
   0.004898529,
   0.003233073,
   0.00291266,
   0.003316045,
   0.004454048,
   0.00667464,
   0.01071829,
   0.01795632,
   0.03085259,
   0.05379965,
   0.09461377,
   0.1671971,
   0.2962732,
   0.5258079,
   0.9339854,
   1.65984,
   2.950611,
   5.245965,
   9.327744,
   16.58629};
   graph = new TGraph(25,Graph2_fx13,Graph2_fy13);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph213 = new TH1F("Graph_Graph213","Graph",100,0.01,10000);
   Graph_Graph213->SetMinimum(0.0001);
   Graph_Graph213->SetMaximum(1);
   Graph_Graph213->SetDirectory(0);
   Graph_Graph213->SetStats(0);
   Graph_Graph213->SetLineStyle(0);
   Graph_Graph213->SetLineWidth(2);
   Graph_Graph213->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph213->GetXaxis()->SetLabelFont(42);
   Graph_Graph213->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph213->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph213->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph213->GetXaxis()->SetTitleOffset(1);
   Graph_Graph213->GetXaxis()->SetTitleFont(42);
   Graph_Graph213->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph213->GetYaxis()->SetLabelFont(42);
   Graph_Graph213->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph213->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph213->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph213->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph213->GetYaxis()->SetTitleFont(42);
   Graph_Graph213->GetZaxis()->SetLabelFont(42);
   Graph_Graph213->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph213->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph213->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph213->GetZaxis()->SetTitleOffset(1);
   Graph_Graph213->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph213);
   
   graph->Draw("l");
   
   Double_t Graph3_fx14[24] = {
   0.02,
   0.03,
   0.04,
   0.05,
   0.06,
   0.1,
   0.125,
   0.2,
   0.3,
   0.5,
   0.7,
   1,
   2,
   3,
   7,
   8,
   20,
   30,
   100,
   200,
   300,
   3000,
   5000,
   10000};
   Double_t Graph3_fy14[24] = {
   2.089613,
   0.2906804,
   0.0895403,
   0.04321463,
   0.02547549,
   0.008395271,
   0.006633915,
   0.003964734,
   0.003170086,
   0.002906099,
   0.002962371,
   0.003197089,
   0.00529421,
   0.00695778,
   0.0137734,
   0.01510565,
   0.0407324,
   0.06181507,
   0.2127993,
   0.4148577,
   0.6169367,
   6.150836,
   9.755892,
   20.29344};
   graph = new TGraph(24,Graph3_fx14,Graph3_fy14);
   graph->SetName("Graph3");
   graph->SetTitle("Graph");
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph314 = new TH1F("Graph_Graph314","Graph",100,0.018,11000);
   Graph_Graph314->SetMinimum(0.002615489);
   Graph_Graph314->SetMaximum(22.3225);
   Graph_Graph314->SetDirectory(0);
   Graph_Graph314->SetStats(0);
   Graph_Graph314->SetLineStyle(0);
   Graph_Graph314->SetLineWidth(2);
   Graph_Graph314->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph314->GetXaxis()->SetLabelFont(42);
   Graph_Graph314->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph314->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph314->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph314->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph314->GetXaxis()->SetTitleFont(42);
   Graph_Graph314->GetYaxis()->SetTitle("95% CL upper limit on B(H ightarrow SS)");
   Graph_Graph314->GetYaxis()->SetLabelFont(42);
   Graph_Graph314->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph314->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph314->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph314->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph314->GetYaxis()->SetTitleFont(42);
   Graph_Graph314->GetZaxis()->SetLabelFont(42);
   Graph_Graph314->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph314->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph314->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph314->GetZaxis()->SetTitleOffset(1);
   Graph_Graph314->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph314);
   
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

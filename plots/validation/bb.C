void bb()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Apr  7 12:39:06 2022) by ROOT version 6.18/02
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
   
   Double_t Graph0_fx9[25] = {
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
   Double_t Graph0_fy9[25] = {
   175.4627,
   3.295121,
   0.2089913,
   0.03239364,
   0.00903619,
   0.003983664,
   0.002523057,
   0.002164323,
   0.002368565,
   0.003086177,
   0.004514868,
   0.007122389,
   0.01179097,
   0.0201095,
   0.03491127,
   0.06123809,
   0.1080575,
   0.1913171,
   0.3393768,
   0.6026688,
   1.070876,
   1.90348,
   3.384081,
   6.017004,
   10.69908};
   TGraph *graph = new TGraph(25,Graph0_fx9,Graph0_fy9);
   graph->SetName("Graph0");
   graph->SetTitle("Graph");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph09 = new TH1F("Graph_Graph09","Graph",100,0.01,10000);
   Graph_Graph09->SetMinimum(0.0001);
   Graph_Graph09->SetMaximum(1);
   Graph_Graph09->SetDirectory(0);
   Graph_Graph09->SetStats(0);
   Graph_Graph09->SetLineStyle(0);
   Graph_Graph09->SetLineWidth(2);
   Graph_Graph09->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph09->GetXaxis()->SetLabelFont(42);
   Graph_Graph09->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph09->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph09->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph09->GetXaxis()->SetTitleOffset(1);
   Graph_Graph09->GetXaxis()->SetTitleFont(42);
   Graph_Graph09->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph09->GetYaxis()->SetLabelFont(42);
   Graph_Graph09->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph09->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph09->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph09->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph09->GetYaxis()->SetTitleFont(42);
   Graph_Graph09->GetZaxis()->SetLabelFont(42);
   Graph_Graph09->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph09->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph09->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph09->GetZaxis()->SetTitleOffset(1);
   Graph_Graph09->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph09);
   
   graph->Draw("la");
   
   Double_t Graph1_fx10[28] = {
   0.02,
   0.03,
   0.04,
   0.05,
   0.06,
   0.1,
   0.125,
   0.2,
   0.3,
   0.6,
   0.7,
   1,
   2,
   3,
   4,
   5,
   6,
   7,
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
   Double_t Graph1_fy10[28] = {
   1.814483,
   0.2256996,
   0.07015441,
   0.03310202,
   0.01901465,
   0.006555388,
   0.005065082,
   0.00316148,
   0.002407052,
   0.002041264,
   0.002013945,
   0.002063958,
   0.003239423,
   0.004237959,
   0.00526897,
   0.006550881,
   0.007473329,
   0.008648584,
   0.01128746,
   0.02253791,
   0.03189327,
   0.1091024,
   0.2181725,
   0.3199817,
   2.119093,
   3.228915,
   5.345636,
   10.63336};
   graph = new TGraph(28,Graph1_fx10,Graph1_fy10);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   
   TH1F *Graph_Graph110 = new TH1F("Graph_Graph110","Graph",100,0.018,11000);
   Graph_Graph110->SetMinimum(0.001812551);
   Graph_Graph110->SetMaximum(11.69649);
   Graph_Graph110->SetDirectory(0);
   Graph_Graph110->SetStats(0);
   Graph_Graph110->SetLineStyle(0);
   Graph_Graph110->SetLineWidth(2);
   Graph_Graph110->GetXaxis()->SetTitle("c#tau [m]");
   Graph_Graph110->GetXaxis()->SetLabelFont(42);
   Graph_Graph110->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph110->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph110->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph110->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph110->GetXaxis()->SetTitleFont(42);
   Graph_Graph110->GetYaxis()->SetTitle("95% CL Limit on BR");
   Graph_Graph110->GetYaxis()->SetLabelFont(42);
   Graph_Graph110->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph110->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph110->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph110->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph110->GetYaxis()->SetTitleFont(42);
   Graph_Graph110->GetZaxis()->SetLabelFont(42);
   Graph_Graph110->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph110->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph110->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph110->GetZaxis()->SetTitleOffset(1);
   Graph_Graph110->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph110);
   
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
   TLegendEntry *entry=leg->AddEntry("Graph0","m_{S} = 15 GeV","L");
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
   entry=leg->AddEntry("Graph1","CMS result","L");
   entry->SetLineColor(1);
   entry->SetLineStyle(2);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph0","this work","L");
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

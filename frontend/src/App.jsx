import { useState } from "react";

function App() {

  const [company, setCompany] = useState("");

  const [results, setResults] = useState(null);

  const [risk, setRisk] = useState(null);

  const [loading, setLoading] = useState(false);


  // ============================================
  // SEARCH FUNCTION
  // ============================================

  const searchMNA = async () => {

    try {

      setLoading(true);

      // M&A API
      const response = await fetch(
        `http://127.0.0.1:8000/mna/${company}`
      );

      const data = await response.json();

      setResults(data);


      // Bankruptcy API
      const riskResponse = await fetch(
        "http://127.0.0.1:8000/bankruptcy-risk"
      );

      const riskData = await riskResponse.json();

      setRisk(riskData);

      setLoading(false);

    } catch (error) {

      console.log(error);

      setLoading(false);

    }
  };


  return (

    <div className="min-h-screen bg-[#020617] text-white p-8">


      {/* ============================================ */}
      {/* HEADER */}
      {/* ============================================ */}

      <div className="mb-12">

        <h1 className="text-6xl font-black tracking-tight mb-3">
          AI Investment Banking Platform
        </h1>

        <p className="text-slate-400 text-lg">
          M&A Intelligence • Bankruptcy Analytics • Comparable Valuation
        </p>

      </div>


      {/* ============================================ */}
      {/* SEARCH BAR */}
      {/* ============================================ */}

      <div className="flex gap-4 mb-12">

        <input
          type="text"
          placeholder="Search company..."
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          className="
            bg-slate-900
            border
            border-slate-700
            rounded-2xl
            px-5
            py-4
            w-[400px]
            text-lg
            outline-none
            focus:border-blue-500
          "
        />

        <button
          onClick={searchMNA}
          className="
            bg-blue-600
            hover:bg-blue-700
            transition-all
            px-8
            py-4
            rounded-2xl
            text-lg
            font-bold
            shadow-lg
          "
        >
          Analyze
        </button>

      </div>


      {/* ============================================ */}
      {/* LOADING */}
      {/* ============================================ */}

      {loading && (

        <div className="text-xl text-blue-400 mb-8 animate-pulse">
          Running AI Financial Analysis...
        </div>

      )}


      {/* ============================================ */}
      {/* TOP DASHBOARD */}
      {/* ============================================ */}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10">


        {/* BANKRUPTCY CARD */}

        {risk && (

          <div className="
            bg-slate-900
            border
            border-slate-800
            rounded-3xl
            p-8
            shadow-2xl
          ">

            <div className="text-slate-400 mb-4 text-sm uppercase tracking-widest">
              Bankruptcy Risk
            </div>

            <div className="text-6xl font-black mb-5">
              {risk.bankruptcy_probability}%
            </div>

            <div
              className={`
                px-4
                py-2
                rounded-full
                w-fit
                font-bold

                ${
                  risk.risk_level === "Low"
                    ? "bg-green-500 text-black"
                    : risk.risk_level === "Moderate"
                    ? "bg-yellow-400 text-black"
                    : "bg-red-500 text-white"
                }
              `}
            >
              {risk.risk_level} Risk
            </div>

          </div>

        )}


        {/* COMPANY OVERVIEW */}

        {results && !results.error && (

          <div className="
            bg-slate-900
            border
            border-slate-800
            rounded-3xl
            p-8
            shadow-2xl
          ">

            <div className="text-slate-400 mb-4 text-sm uppercase tracking-widest">
              Target Company
            </div>

            <h2 className="text-4xl font-black mb-3">
              {results.target_company}
            </h2>

            <p className="text-blue-400 text-xl mb-6">
              {results.target_sector}
            </p>

            <div className="space-y-3 text-slate-300">

              <div className="flex justify-between">
                <span>Analysis Engine</span>
                <span className="font-bold text-green-400">
                  Active
                </span>
              </div>

              <div className="flex justify-between">
                <span>Strategic Matches</span>
                <span className="font-bold">
                  {results.recommended_acquirers.length}
                </span>
              </div>

              <div className="flex justify-between">
                <span>Data Source</span>
                <span className="font-bold">
                  Live Market Data
                </span>
              </div>

            </div>

          </div>

        )}


        {/* AI COMMENTARY */}

        {results && !results.error && (

          <div className="
            bg-slate-900
            border
            border-slate-800
            rounded-3xl
            p-8
            shadow-2xl
          ">

            <div className="text-slate-400 mb-4 text-sm uppercase tracking-widest">
              AI Analyst Commentary
            </div>

            <p className="text-slate-300 leading-8 text-lg">
              {results.target_company} demonstrates strategic relevance within
              the {results.target_sector} sector. The platform identified
              multiple acquisition candidates based on financial scale,
              strategic compatibility, and sector alignment.
            </p>

          </div>

        )}

      </div>


      {/* ============================================ */}
      {/* ACQUIRER CARDS */}
      {/* ============================================ */}

      {results && !results.error && (

        <div>

          <div className="flex items-center justify-between mb-8">

            <h2 className="text-4xl font-black">
              Recommended Acquirers
            </h2>

            <div className="text-slate-400">
              AI Strategic Screening Results
            </div>

          </div>


          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

            {results.recommended_acquirers.map((item, index) => (

              <div
                key={index}
                className="
                  bg-slate-900
                  border
                  border-slate-800
                  rounded-3xl
                  p-8
                  shadow-2xl
                  hover:border-blue-500
                  transition-all
                "
              >


                {/* HEADER */}

                <div className="flex justify-between items-start mb-6">

                  <div>

                    <h3 className="text-3xl font-black mb-2">
                      {item.acquirer}
                    </h3>

                    <p className="text-blue-400 text-lg">
                      {item.sector}
                    </p>

                  </div>


                  <div className="text-right">

                    <div className="text-4xl font-black text-green-400">
                      {item.acquisition_probability}%
                    </div>

                    <div className="text-slate-400 text-sm">
                      Acquisition Probability
                    </div>

                  </div>

                </div>


                {/* PROGRESS BAR */}

                <div className="mb-6">

                  <div className="w-full bg-slate-800 rounded-full h-4 overflow-hidden">

                    <div
                      className="bg-green-500 h-4 rounded-full transition-all duration-700"
                      style={{
                        width: `${item.acquisition_probability}%`
                      }}
                    ></div>

                  </div>

                </div>


                {/* METRICS */}

                <div className="grid grid-cols-2 gap-4 mb-6">

                  <div className="bg-slate-800 rounded-2xl p-4">

                    <div className="text-slate-400 text-sm mb-1">
                      Industry
                    </div>

                    <div className="font-bold">
                      {item.industry}
                    </div>

                  </div>


                  <div className="bg-slate-800 rounded-2xl p-4">

                    <div className="text-slate-400 text-sm mb-1">
                      Market Cap
                    </div>

                    <div className="font-bold">
                      ${item.market_cap}B
                    </div>

                  </div>

                </div>


                {/* RATIONALE */}

                <div className="bg-slate-800 rounded-2xl p-5">

                  <div className="text-slate-400 text-sm mb-3 uppercase tracking-widest">
                    Strategic Rationale
                  </div>

                  <p className="leading-8 text-slate-300">
                    {item.rationale}
                  </p>

                </div>

              </div>

            ))}

          </div>

        </div>

      )}


      {/* ============================================ */}
      {/* ERROR */}
      {/* ============================================ */}

      {results && results.error && (

        <div className="
          bg-red-500
          p-5
          rounded-2xl
          text-lg
          font-bold
          w-fit
        ">
          {results.error}
        </div>

      )}

    </div>
  );
}

export default App;
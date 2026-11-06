import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang9_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                y=symbols('y')
                i=randint(1,9)
                x0=2*i
                y0=4*i
                a=4*i
                b=3*i
                r=i
                m=Rational(y0,x0**2)

                c=(x-a)**2+(y-b)**2

                f=expand((a-x)**2+(b-y0+m*x**2)**2)
                daoham=diff(f, x)
                nghiem=solve(daoham, x)
                n0=[sol.evalf() for sol in nghiem if sol.is_real]

                solution_str = ', '.join(map(str, n0))
                solution_str

                n1 = n0[-1]

                fn1=expand((a-n1)**2+(b-y0+m*n1**2)**2)
                f0=expand((a-0)**2+(b-y0+m*0**2)**2)
                fx0=expand((a-x0)**2+(b-y0+m*x0**2)**2)
                zz=sqrt(fn1)
                h1=10*round(sqrt(fn1),2)-10*r
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{ Một cái ao hình $ABCDE$, ở giữa ao có một mảnh vườn hình tròn có bán kính $%s0$ m. Người ta muốn bắc một chiếc cầu từ bờ $AB$ của ao đến vườn. '
                                'Biết hai bờ $AE$ và $BC$ nằm trêm hai đường thẳng vuông góc với nhau, hai đường thẳng này cắt nhau tại điểm $O$. '
                                'Bờ $AB$ là một phần của parabol có đỉnh là điểm $A$ và có trục đối xứng là đường thẳng $OA$. '
                                'Độ dài $OA$ và $OB$ lần lượt là $%s0$ m và $%s0$ m. '
                                'Tâm $I$ của mảnh vườn lần lượt cách các đường thẳng $AE$ và $BC$ là $%s0$ m và $%s0$ m. '
                                'Độ dài tối thiểu của cây cầu là bao nhiêu mét? (kết quả làm tròn đến hàng đơn vị). }'
                                '{'
                                '\\scalebox{0.7}{ '
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]    \n'
                                    '\\clip(-0.6735761640695058,-0.5979787848349137) rectangle (6.70630238315673,5.739188542563963);  \n'
                                    '\\draw [samples=50,rotate around={-180.:(0.,3.)},xshift=0.cm,yshift=3.cm,domain=-1.74:0)] plot (\\x,{(\\x)^2/2/0.5});  \n'
                                    '\\draw (0.,3.)-- (0.,5.);  \n'
                                    '\\draw (1.7320508075688774,0.)-- (6.,0.);  \n'
                                    '\\draw (6.,0.)-- (6.,5.);  \n'
                                    '\\draw (6.,5.)-- (0.,5.);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0.,3.)-- (0.,0.);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (1.7320508075688774,0.);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0.,2.)-- (4.,2.);  \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (4.,2.)-- (4.,0.);  \n'
                                    '\\draw(4.,2.) circle (1.cm);  \n'
                                    '\\draw (3.0368644673666103,1.7309833726718802)-- (1.33593118747405,1.2152878623341745);  \n'
                                    '\\draw (1.3828133581349062,1.0878272165636635)-- (3.0790081238941225,1.6104182189231948);  \n'
                                    '\\draw [dotted] (0.1755163996500514,4.783526607866321)-- (5.807413400546958,4.795355110823705);  \n'
                                    '\\draw [dotted] (0.1755163996500514,4.499564130816353)-- (5.816904277042762,4.471167883111356);  \n'
                                    '\\draw [dotted] (0.16605098374838578,4.20613623786472)-- (5.827166272591045,4.2302508792612);  \n'
                                    '\\draw [dotted] (0.18498181555171703,3.931639176716417)-- (5.840381616727836,3.9461209803201984);  \n'
                                    '\\draw [dotted] (0.16605098374838578,3.6666075314697806)-- (5.83377394465944,3.655383409310802);  \n'
                                    '\\draw [dotted] (0.1755163996500514,3.3921104703214784)-- (5.83377394465944,3.358038166233011);  \n'
                                    '\\draw [dotted] (0.19444723145338264,3.1460096568781726)-- (5.827166272591045,3.1201619717707776);  \n'
                                    '\\draw [dotted] (0.5068059562083481,2.9377705070415296)-- (3.2896382312980412,2.909374259336533);  \n'
                                    '\\draw [dotted] (0.7245105219466574,2.6916696935982243)-- (3.128726160969726,2.6822042776965587);  \n'
                                    '\\draw [dotted] (0.885422592274973,2.4739651278599153)-- (2.9867449224447413,2.483430543761581);  \n'
                                    '\\draw [dotted] (1.0179384148982917,2.22786431441661)-- (2.873159931624754,2.246795146219941);  \n'
                                    '\\draw [dotted] (4.756777696056212,2.880978011631536)-- (5.83377394465944,2.895501121445335);  \n'
                                    '\\draw [dotted] (4.93662059818786,2.625411782286565)-- (5.83377394465944,2.6311942387095204);  \n'
                                    '\\draw [dotted] (5.02180934130285,2.3603801370399284)-- (5.83377394465944,2.3602796839053104);  \n'
                                    '\\draw [dotted] (5.116463500319506,2.1710718190066163)-- (5.83377394465944,2.168657193921845);  \n'
                                    '\\draw [dotted] (5.1353943321228375,1.924971005563311)-- (5.846989288796231,1.9175656553228209);  \n'
                                    '\\draw [dotted] (5.093714672999157,1.6995124770657737)-- (5.846989288796231,1.6796894608605877);  \n'
                                    '\\draw [dotted] (5.841042383934675,1.4041495356085003)-- (4.93662059818786,1.4043731309717031);  \n'
                                    '\\draw [dotted] (5.83377394465944,1.1642910395257486)-- (4.71891603244955,1.1582723175283975);  \n'
                                    '\\draw [dotted] (5.826505505384206,0.8953587863420572)-- (1.5858633689982289,0.9027060881834266);  \n'
                                    '\\draw [dotted] (1.6615866962115537,0.6755361065434522)-- (5.81923706610897,0.6845740473602451);  \n'
                                    '\\draw [dotted] (1.737310023424879,0.4294352931001468)-- (5.826505505384206,0.46652086910319807);  \n'
                                    '\\draw [dotted] (1.792521707628823,0.2121254944699765)-- (5.826505505384206,0.23393081229568122);  \n'
                                    '\\draw [dotted] (1.2261775647349353,1.8019205988416582)-- (2.8636945157230884,1.8113860147433238);  \n'
                                    '\\draw [dotted] (1.3302971396532572,1.5368889535950214)-- (2.144322907196501,1.5368889535950214);  \n'
                                    '\\draw [dotted] (1.7467754393265447,1.082548990315073)-- (3.3748269744130317,1.1109452380200697);  \n'
                                    '\\draw [dotted] (2.286304145721485,1.2813227242500504)-- (3.1097953291663947,1.3002535560533817);  \n'
                                    '\\draw [dotted] (2.825832852116426,1.4422347945783656)-- (3.0530028337564006,1.4422347945783656);  \n'
                                    '\\draw (-0.4848094777214535,3.56387720464832) node[anchor=north west] {$A$};  \n'
                                    '\\draw (1.3399351569763858,0.04023239281802274) node[anchor=north west] {$B$};  \n'
                                    '\\draw (5.99618008689501,0.11214351142680432) node[anchor=north west] {$C$};  \n'
                                    '\\draw (6.077080095329889,5.550421856215911) node[anchor=north west] {$D$};  \n'
                                    '\\draw (-0.34098724050388984,5.604355195172497) node[anchor=north west] {$E$};  \n'
                                    '\\draw (4.0455909946318025,2.5750993237775734) node[anchor=north west] {$I$};  \n'
                                    '\\draw (-0.5387428166780399,2.0357659342117116) node[anchor=north west] {$%s0$};  \n'
                                    '\\draw (0.6208239708885673,0.5795657823838846) node[anchor=north west] {$%s0$};  \n'
                                    '\\draw (1.6365685212376109,2.530154874647085) node[anchor=north west] {$%s0$};  \n'
                                    '\\draw (4.090535443762291,1.0919325024714532) node[anchor=north west] {$%s0$};  \n'
                                    '\\draw (-0.5,0) node[anchor=north west] {$O$};  \n'
                                '\\end{tikzpicture} } \n'
                                '}'
                                %(latex(r),
                                latex(y0),latex(x0),
                                latex(a),latex(b),
                                latex(y0),
                                latex(x0),
                                latex(a),
                                latex(b),                         
                                    ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                            '\\scalebox{0.7}{ '
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]    \n'
                            '\\clip(-0.6735761640695058,-0.5979787848349137) rectangle (6.70630238315673,5.739188542563963);  \n'
                            '\\draw [samples=50,rotate around={-180.:(0.,3.)},xshift=0.cm,yshift=3.cm,domain=-1.74:0)] plot (\\x,{(\\x)^2/2/0.5});  \n'
                            '\\draw (0.,3.)-- (0.,5.);  \n'
                            '\\draw (1.7320508075688774,0.)-- (6.,0.);  \n'
                            '\\draw (6.,0.)-- (6.,5.);  \n'
                            '\\draw (6.,5.)-- (0.,5.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,3.)-- (0.,0.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (1.7320508075688774,0.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,2.)-- (4.,2.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (4.,2.)-- (4.,0.);  \n'
                            '\\draw(4.,2.) circle (1.cm);  \n'
                            '\\draw (3.0368644673666103,1.7309833726718802)-- (1.33593118747405,1.2152878623341745);  \n'
                            '\\draw (1.3828133581349062,1.0878272165636635)-- (3.0790081238941225,1.6104182189231948);  \n'
                            '\\draw [dotted] (0.1755163996500514,4.783526607866321)-- (5.807413400546958,4.795355110823705);  \n'
                            '\\draw [dotted] (0.1755163996500514,4.499564130816353)-- (5.816904277042762,4.471167883111356);  \n'
                            '\\draw [dotted] (0.16605098374838578,4.20613623786472)-- (5.827166272591045,4.2302508792612);  \n'
                            '\\draw [dotted] (0.18498181555171703,3.931639176716417)-- (5.840381616727836,3.9461209803201984);  \n'
                            '\\draw [dotted] (0.16605098374838578,3.6666075314697806)-- (5.83377394465944,3.655383409310802);  \n'
                            '\\draw [dotted] (0.1755163996500514,3.3921104703214784)-- (5.83377394465944,3.358038166233011);  \n'
                            '\\draw [dotted] (0.19444723145338264,3.1460096568781726)-- (5.827166272591045,3.1201619717707776);  \n'
                            '\\draw [dotted] (0.5068059562083481,2.9377705070415296)-- (3.2896382312980412,2.909374259336533);  \n'
                            '\\draw [dotted] (0.7245105219466574,2.6916696935982243)-- (3.128726160969726,2.6822042776965587);  \n'
                            '\\draw [dotted] (0.885422592274973,2.4739651278599153)-- (2.9867449224447413,2.483430543761581);  \n'
                            '\\draw [dotted] (1.0179384148982917,2.22786431441661)-- (2.873159931624754,2.246795146219941);  \n'
                            '\\draw [dotted] (4.756777696056212,2.880978011631536)-- (5.83377394465944,2.895501121445335);  \n'
                            '\\draw [dotted] (4.93662059818786,2.625411782286565)-- (5.83377394465944,2.6311942387095204);  \n'
                            '\\draw [dotted] (5.02180934130285,2.3603801370399284)-- (5.83377394465944,2.3602796839053104);  \n'
                            '\\draw [dotted] (5.116463500319506,2.1710718190066163)-- (5.83377394465944,2.168657193921845);  \n'
                            '\\draw [dotted] (5.1353943321228375,1.924971005563311)-- (5.846989288796231,1.9175656553228209);  \n'
                            '\\draw [dotted] (5.093714672999157,1.6995124770657737)-- (5.846989288796231,1.6796894608605877);  \n'
                            '\\draw [dotted] (5.841042383934675,1.4041495356085003)-- (4.93662059818786,1.4043731309717031);  \n'
                            '\\draw [dotted] (5.83377394465944,1.1642910395257486)-- (4.71891603244955,1.1582723175283975);  \n'
                            '\\draw [dotted] (5.826505505384206,0.8953587863420572)-- (1.5858633689982289,0.9027060881834266);  \n'
                            '\\draw [dotted] (1.6615866962115537,0.6755361065434522)-- (5.81923706610897,0.6845740473602451);  \n'
                            '\\draw [dotted] (1.737310023424879,0.4294352931001468)-- (5.826505505384206,0.46652086910319807);  \n'
                            '\\draw [dotted] (1.792521707628823,0.2121254944699765)-- (5.826505505384206,0.23393081229568122);  \n'
                            '\\draw [dotted] (1.2261775647349353,1.8019205988416582)-- (2.8636945157230884,1.8113860147433238);  \n'
                            '\\draw [dotted] (1.3302971396532572,1.5368889535950214)-- (2.144322907196501,1.5368889535950214);  \n'
                            '\\draw [dotted] (1.7467754393265447,1.082548990315073)-- (3.3748269744130317,1.1109452380200697);  \n'
                            '\\draw [dotted] (2.286304145721485,1.2813227242500504)-- (3.1097953291663947,1.3002535560533817);  \n'
                            '\\draw [dotted] (2.825832852116426,1.4422347945783656)-- (3.0530028337564006,1.4422347945783656);  \n'
                            '\\draw (-0.4848094777214535,3.56387720464832) node[anchor=north west] {$A$};  \n'
                            '\\draw (1.3399351569763858,0.04023239281802274) node[anchor=north west] {$B$};  \n'
                            '\\draw (5.8,0) node[anchor=north west] {$C$};    \n'
                            '\\draw (6.077080095329889,5.550421856215911) node[anchor=north west] {$D$};  \n'
                            '\\draw (0,5.604355195172497) node[anchor=north west] {$E$};    \n'
                            '\\draw (4.0455909946318025,2.5750993237775734) node[anchor=north west] {$I$};  \n'
                            '\\draw (-0.5387428166780399,2.0357659342117116) node[anchor=north west] {$%s0$};  \n'
                            '\\draw (0.6208239708885673,0.5795657823838846) node[anchor=north west] {$%s0$};  \n'
                            '\\draw (1.6365685212376109,2.530154874647085) node[anchor=north west] {$%s0$};  \n'
                            '\\draw (4.090535443762291,1.0919325024714532) node[anchor=north west] {$%s0$};  \n'
                            '\\draw (-0.5,0) node[anchor=north west] {$O$};  \n'
                            '\\draw (0.7,1.5) node[anchor=north west] {$N$}; '
                            '\\draw (3,2) node[anchor=north west] {$M$}; '
                            '\\draw[->] (-2,0)--(6.5,0) node[above] {$x$};' 
                            '\\draw[->] (0,-3)--(0,5.5) node[below left] {$y$}; '
                        '\\end{tikzpicture} } \n'
                        '\\end{center} \n'

                            'Gán hệ trục tọa độ $(Oxy)$ sao cho điểm $O$ trùng với gốc tọa độ, $\\heva{& A \\in Ox \\\\ & B \\in Oy}$ với đơn vị là $10$. \\\\ \n'
                        'Khi đó mảnh vườn hình tròn có phương trình $(C): %s=%s$ có tâm $I(%s;%s)$. \\\\ \n' #1
                        'Bờ $AB$ là một phần của parabol $(P): y=%s-%sx^2$ trên đoạn $[0;%s]$. \\\\ \n' #2
                        'Bài toán trở thành tìm $MN$ nhỏ nhất với $\\heva{& N \\in (P) \\\\ & M \\in (C)}$. \\\\ \n'
                        'Khi đó $MN + MI \\ge IN$, suy ra $MN$ nhỏ nhất khi $MN+MI=IN$ hay ba điểm $M, N, I$ thẳng hàng. \\\\ \n'
                        'Sau đây ta xác định điểm $N$ để $IN$ nhỏ nhất. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $N \\in (P) \\Rightarrow N(x;%s-x^2)$. \\\\ \n' #3
                        '\\hspace*{1cm} $IN =\\sqrt{(%s-x)^2+\\left(%s+%sx^2\\right)^2} \\Leftrightarrow IN^2 =(%s-x)^2+\\left(%s+%sx^2\\right)^2=%s$. \\\\ \n' #4
                        'Xét hàm số $f(x)=%s$ trên đoạn $[0;%s]$. \\\\ \n' #5
                        '\\hspace*{1cm} $f\'(x)=%s$. \\\\ \n' #6
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow x \\approx %s$. \\\\ \n' #7
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $f(%s) \\approx %s$. \\\\ \n' #8
                        '\\hspace*{1cm} $f(0)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $f(%s)=%s$. \\\\ \n'
                        'Suy ra giá trị nhỏ nhất của hàm số $f(x)$ trên đoạn $[0;%s]$ bằng $%s$ khi $x \\approx %s$. \\\\ \n'
                        'Do đó $\\min IN = \\sqrt{%s} = %s \\Rightarrow IN=%s$ m. \\\\ \n'
                        'Suy ra $MN=IN-IM=%s-%s=%s$ m. \\\\ \n'
                        'Vậy độ dài tối tiểu của cây cầu là $%s$ m.'
                        %(latex(y0),
                        latex(x0),
                        latex(a),
                        latex(b),
                            latex(c),latex(r**2),latex(a),latex(b), #1 
                            latex(y0),latex(m),latex(x0), #2
                            latex(y0), #3
                            latex(a),latex(b-y0),latex(m),latex(a),latex(b-y0),latex(m),latex(f), #4
                            latex(f),latex(x0), #5
                            latex(daoham), #6
                            latex(round(n1,2)), #7
                            latex(round(n1,2)),latex(round(fn1,2)), #8
                            latex(f0),
                            latex(x0),latex(fx0),
                            latex(x0),latex(round(fn1,2)), latex(round(n1,2)),
                            latex(round(fn1,2)),latex(round(sqrt(fn1),2)),latex(10*round(sqrt(fn1),2)),
                            latex(10*round(sqrt(fn1),2)),latex(10*r),latex(10*round(sqrt(fn1),2)-10*r),
                            latex(kq)
                        ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content


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


def bt_dang16_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                b=randint(1,5)
                a=3*b
                c=6*b

                # Khai báo biến
                x, y, z = symbols('x y z')

                # Định nghĩa hệ phương trình
                eq1 = Eq(0*x + 0*y + z, c)
                eq2 = Eq(a**2*x +a*y + z, 0)
                eq3 = Eq(b**2*x +b*y + z, Rational(c,2))

                # Giải hệ phương trình
                solution = solve((eq1, eq2, eq3), (x, y, z))

                # Tách từng nghiệm
                a0 = solution[x]
                b0 = solution[y]
                c0 = solution[z]

                f=a0*x**2+b0*x+c0

                x0=(-b0+sqrt(b0**2-4*a0*c0+4*a0*y))/(2*a0)
                x01=(-b0-sqrt(b0**2-4*a0*c0+4*a0*y))/(2*a0)

                f1=(3*sqrt(3)/2)*x01

                s1 = integrate((3*sqrt(3)/2)*x01**2, (y, 0, c))

                h1=s1   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Người ta dựng một cái lều vải (H) có dạng hình "chóp lục giác cong đều" như hình vẽ. Đáy của (H) là một hình lục giác đều cạnh bằng $%s$ m, chiều cao $SO=%s$ m. Các cạnh bên của (H) là các sợi dây $c_1, c_2, c_3, c_4, c_5, c_6$ nằm trên các đường parabol có trục đối xứng song song với $SO$. Giả sử giao tuyến nếu có của (H) với mặt phẳng $(P)$ vuông góc với $SO$ là một lục giác đều và khi $(P)$ qua trung điểm của $SO$ thì lục giác đều có cạnh bằng $%s$ m. Thể tích phần không gian bên trong (H) là bao nhiêu mét khối? (làm tròn kết quả đến hàng đơn vị).}{
                    \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.031738615949694134,-0.08346486166631074) rectangle (5.027835522532472,5.236726772403759);
                    \\draw [line width=1.pt] (0.17579278887500963,1.801225828005587)-- (0.5612192190263934,0.6082392584894006);
                    \\draw [line width=1.pt] (0.5612192190263934,0.6082392584894006)-- (2.8462473406381683,0.14939827021394433);
                    \\draw [line width=1.pt] (2.8462473406381683,0.14939827021394433)-- (4.773379491395087,0.9386047700477291);
                    \\draw [line width=1.pt] (4.773379491395087,0.9386047700477291)-- (4.369599421712685,2.1315913395639154);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (4.369599421712685,2.1315913395639154)-- (2.0662176605698916,2.5812555080738626);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.0662176605698916,2.5812555080738626)-- (0.17579278887500963,1.801225828005587);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.17579278887500963,1.801225828005587)-- (4.773379491395087,0.9386047700477291);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (4.369599421712685,2.1315913395639154)-- (0.5612192190263934,0.6082392584894006);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.0662176605698916,2.5812555080738626)-- (2.8462473406381683,0.14939827021394433);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.468339419071842,1.371087338507579)-- (2.479174550017803,4.691924054140961);
                    \\draw [line width=1.pt] (1.7083216897150353,3.1869256125974648)-- (1.827620346666654,2.7556150836185362);
                    \\draw [line width=1.pt] (1.827620346666654,2.7556150836185362)-- (2.592052643276087,2.6285063380912033);
                    \\draw [line width=1.pt] (2.592052643276087,2.6285063380912033)-- (3.2248384077308665,2.8790378448345244);
                    \\draw [line width=1.pt] (3.2248384077308665,2.8790378448345244)-- (3.1111952500328655,3.281954494854711);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.1111952500328655,3.281954494854711)-- (2.3431545483214458,3.4239007444966374);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.3431545483214458,3.4239007444966374)-- (1.7083216897150353,3.1869256125974648);
                    \\draw [shift={(-9.056516118030698,9.650535784487262)},line width=1.pt]  plot[domain=5.742444323208742:5.8772142074805975,variable=\\t]({1.*12.556272913616892*cos(\\t r)+0.*12.556272913616892*sin(\\t r)},{0.*12.556272913616892*cos(\\t r)+1.*12.556272913616892*sin(\\t r)});
                    \\draw [shift={(-2.067876491869508,5.385581499631687)},line width=1.pt]  plot[domain=5.506113876026303:5.755926551705518,variable=\\t]({1.*4.369640765119331*cos(\\t r)+0.*4.369640765119331*sin(\\t r)},{0.*4.369640765119331*cos(\\t r)+1.*4.369640765119331*sin(\\t r)});
                    \\draw [shift={(-0.3032217114006937,3.5940462176388137)},line width=1.pt]  plot[domain=4.973475118608931:5.527640957175722,variable=\\t]({1.*1.8557100638189732*cos(\\t r)+0.*1.8557100638189732*sin(\\t r)},{0.*1.8557100638189732*cos(\\t r)+1.*1.8557100638189732*sin(\\t r)});
                    \\draw [shift={(-48.55439627166523,20.78658167371641)},line width=1.pt]  plot[domain=5.939503356605567:5.977684346063967,variable=\\t]({1.*53.51133856205708*cos(\\t r)+0.*53.51133856205708*sin(\\t r)},{0.*53.51133856205708*cos(\\t r)+1.*53.51133856205708*sin(\\t r)});
                    \\draw [shift={(-7.980297809226008,6.559309564513497)},line width=1.pt]  plot[domain=5.784394875585262:5.913223918842008,variable=\\t]({1.*10.519664930817887*cos(\\t r)+0.*10.519664930817887*sin(\\t r)},{0.*10.519664930817887*cos(\\t r)+1.*10.519664930817887*sin(\\t r)});
                    \\draw [shift={(-1.4851687816235837,2.882692271596711)},line width=1.pt]  plot[domain=5.445053528065798:5.824159913688012,variable=\\t]({1.*3.0595490448817992*cos(\\t r)+0.*3.0595490448817992*sin(\\t r)},{0.*3.0595490448817992*cos(\\t r)+1.*3.0595490448817992*sin(\\t r)});
                    \\draw [shift={(-113.46842506617534,-2.6857197993377806)},line width=1.pt]  plot[domain=0.045756462559716875:0.06354345806452077,variable=\\t]({1.*116.18207902075865*cos(\\t r)+0.*116.18207902075865*sin(\\t r)},{0.*116.18207902075865*cos(\\t r)+1.*116.18207902075865*sin(\\t r)});
                    \\draw [shift={(32.922623998326806,4.485857612079132)},line width=1.pt]  plot[domain=3.20275321651503:3.2847874098583723,variable=\\t]({1.*30.38738739146239*cos(\\t r)+0.*30.38738739146239*sin(\\t r)},{0.*30.38738739146239*cos(\\t r)+1.*30.38738739146239*sin(\\t r)});
                    \\draw [shift={(17.293553611020844,9.725478556960944)},line width=1.pt]  plot[domain=3.4691293922030373:3.594497617214876,variable=\\t]({1.*15.646165597230032*cos(\\t r)+0.*15.646165597230032*sin(\\t r)},{0.*15.646165597230032*cos(\\t r)+1.*15.646165597230032*sin(\\t r)});
                    \\draw [shift={(14.438073375223327,8.659544317720309)},line width=1.pt]  plot[domain=3.617569140105847:3.725237417898989,variable=\\t]({1.*12.61550211126256*cos(\\t r)+0.*12.61550211126256*sin(\\t r)},{0.*12.61550211126256*cos(\\t r)+1.*12.61550211126256*sin(\\t r)});
                    \\draw [shift={(5.8738274815705696,3.0409938328429185)},line width=1.pt]  plot[domain=3.738316955168666:4.2301756030068836,variable=\\t]({1.*2.3729782026900486*cos(\\t r)+0.*2.3729782026900486*sin(\\t r)},{0.*2.3729782026900486*cos(\\t r)+1.*2.3729782026900486*sin(\\t r)});
                    \\draw [shift={(7.635182034671983,6.156474323650794)},line width=1.pt]  plot[domain=3.418350506919084:3.7076323236019015,variable=\\t]({1.*5.359973943381745*cos(\\t r)+0.*5.359973943381745*sin(\\t r)},{0.*5.359973943381745*cos(\\t r)+1.*5.359973943381745*sin(\\t r)});
                    \\draw [shift={(5.991679693819027,4.711368264545467)},line width=1.pt]  plot[domain=3.6022283451518513:3.9222072208241587,variable=\\t]({1.*3.215651466791077*cos(\\t r)+0.*3.215651466791077*sin(\\t r)},{0.*3.215651466791077*cos(\\t r)+1.*3.215651466791077*sin(\\t r)});
                    \\draw [shift={(4.553304248322953,3.366884657738641)},line width=1.pt]  plot[domain=3.967846222277681:4.564757433600645,variable=\\t]({1.*1.2488783148277622*cos(\\t r)+0.*1.2488783148277622*sin(\\t r)},{0.*1.2488783148277622*cos(\\t r)+1.*1.2488783148277622*sin(\\t r)});
                    \\draw [shift={(35.398907447034816,0.5193395585835593)},line width=1.pt,dash pattern=on 2pt off 2pt]  plot[domain=3.0155147052060394:3.053949199344199,variable=\\t]({1.*33.18311732468049*cos(\\t r)+0.*33.18311732468049*sin(\\t r)},{0.*33.18311732468049*cos(\\t r)+1.*33.18311732468049*sin(\\t r)});
                    \\draw [shift={(-1.497481603561138,3.7579395083178295)},line width=1.pt,dash pattern=on 2pt off 2pt]  plot[domain=6.027124056760866:6.1964287750784806,variable=\\t]({1.*3.855135269595952*cos(\\t r)+0.*3.855135269595952*sin(\\t r)},{0.*3.855135269595952*cos(\\t r)+1.*3.855135269595952*sin(\\t r)});
                    \\draw [shift={(1.3955158859303214,3.004609711289813)},line width=1.pt,dash pattern=on 2pt off 2pt]  plot[domain=5.787911231424192:6.022563073875551,variable=\\t]({1.*0.8656753128295473*cos(\\t r)+0.*0.8656753128295473*sin(\\t r)},{0.*0.8656753128295473*cos(\\t r)+1.*0.8656753128295473*sin(\\t r)});
                    \\draw [shift={(2.1089076320607734,2.6084733095581862)},line width=1.pt]  plot[domain=3.709179322247784:5.976276483018757,variable=\\t]({1.*0.05062847403914465*cos(\\t r)+0.*0.05062847403914465*sin(\\t r)},{0.*0.05062847403914465*cos(\\t r)+1.*0.05062847403914465*sin(\\t r)});
                    \\draw (2,1.4083456303195532) node[anchor=north west] {$O$};
                    \\draw (2.2,5.182805911247643) node[anchor=north west] {$S$};
                    \\draw (0.6,2.801301210185872) node[anchor=north west] {$c_1$};
                    \\draw (1.4420982556507949,1.9655278622660808) node[anchor=north west] {$c_2$};
                    \\draw (2.6,1.9924882928441385) node[anchor=north west] {$c_3$};
                    \\draw (3.2,2.2351321680466585) node[anchor=north west] {$c_4$};
                    \\draw (3.598932701895413,2.945090173268847) node[anchor=north west] {$c_5$};
                    \\draw (1.8,3.2057076688567387) node[anchor=north west] {$c_6$};
                    \\draw (2.7,2.82826164076393) node[anchor=north west] {$%s$m};
                    \\draw (3.7517084751710734,0.6085195231705057) node[anchor=north west] {$%s$m};
            \\end{tikzpicture}}'''
                                %(latex(a),latex(c),latex(b),latex(b),latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('''Chọn trục tọa độ $Oy$ trùng với $OS$ và $Ox$ trùng với $OA_1$. \\\\
                        \\begin{center}
                        \\scalebox{0.6}{ 
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.0707037423261125,-1.0194411432345514) rectangle (4.04009521425436,7.136089106627933);	
                    \\draw[domain=0:3,samples=100,smooth,thick,red] 
                    plot (\\x,{0.5*(\\x)^2 - 3.5*(\\x) + 6});
                    \\draw [line width=1.pt] (1.,3.)-- (0.,3.);
                    \\draw [line width=1.pt] (1.,3.)-- (1.,0.);
                    \\draw [->,line width=1.pt] (-1.,0.) -- (4.,0.);
                    \\draw [->,line width=1.pt] (0.,-1.) -- (0.,7.);
                    \\draw (-0.55,0) node[anchor=north west] {$O$};
                    \\draw (3.594259560595212,-0.1) node[anchor=north west] {$x$};
                    \\draw (-0.5,7.103466985628484) node[anchor=north west] {$y$};
                    \\draw (0.8,0.07883693041359666) node[anchor=north west] {$%s$};
                    \\draw (2.7,0.08971097074674664) node[anchor=north west] {$%s$};
                    \\draw (-0.5,3.3410490303585907) node[anchor=north west] {$%s$};
                    \\draw (-0.5,6.277039920309085) node[anchor=north west] {$%s$};
                    \\draw (-0.1,6.461898605972634) node[anchor=north west] {$S$};
                    \\draw (2.9,0.5572947050721958) node[anchor=north west] {$A_1$};
                    \\draw (0.7778831143093775,4.210972257010589) node[anchor=north west] {$c_1$};
                \\end{tikzpicture} }
            \\end{center}
                        Phương trình đường cong parabol $c_1$ là $y=ax^2+bx+c$ đi qua các điểm $(0;%s), (%s;0), (%s;%s)$. \\\\
                            Do đó \\\\
                            $\\heva{&c=%s \\\\& %sa+%sb+c=0 \\\\& %sa+%sb+c=%s} \\Leftrightarrow \\heva{&a=%s \\\\& b=%s \\\\& c=%s}$. Suy ra $y=%s$. \\\\
                        Khi cắt (H) bởi mặt phẳng vuông góc với trục $Oy$ tại điểm có tung độ $y$ $(0\\le y \\le %s)$ ta được thiết diện là một hình lục giác đều có độ dài cạnh $x$ được xác định bởi $y=%s$.
                        Giải phương trình bậc hai ẩn $x$, rút ra $x=%s$ và $x=%s$. \\\\
                            Vì $0 \\le x \\le %s$ nên nhận $x=%s$. \\\\
                        Do đó diện tích thiết diện vuông góc với trục $Oy$ tại điểm có tung độ $y$ $(0 \\le y \\le %s)$ là \\\\
                            $S(y)=6 \\cdot \\frac{x^2 \\sqrt{3}}{4}=\\frac{3 \\sqrt{3}}{2} \\left(%s \\right)^2$. \\\\
                        Vậy thể tích của (H) là \\\\
                            $V_{Oy}=\\int \\limits_0^{%s} S(y) \\text{d}y = \\int \\limits_0^{%s} \\frac{3 \\sqrt{3}}{2} \\left( %s \\right)^2 \\text{d}y=%s  \\approx %s$ m$^3$.'''
                            %(latex(b),latex(a),latex(Rational(c,2)),latex(c),
                            latex(c),latex(a),latex(b),latex(Rational(c,2)),
                            latex(c),latex(a**2),latex(a),
                            latex(b**2),latex(b),latex(Rational(c,2)),
                            latex(a0),latex(b0),latex(c0),
                            latex(f),
                            latex(c),latex(f),
                            latex(x0),latex(x01),
                            latex(a),latex(x01),
                            latex(c),
                            latex(x01),latex(c),latex(c),latex(x01),latex(s1),
                            latex(kq)
                                ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 


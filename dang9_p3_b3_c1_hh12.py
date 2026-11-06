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


def bt_dang9_p3_b3_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                k=randint(1,3)
                a=8*k
                b=6*k
                c=4*k
                d=3*k
                e=2*k
                kc=sqrt((e-Rational(b,2))**2+(d-Rational(a,2))**2)
                h1=kc   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq=str(kq1).replace('.', ',')
                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Trong một căn phòng dạng hình hộp chữ nhật với chiều dài $%s$ m, rộng $%s$ m và cao $%s$ m có một cây quạt trần $A$ ở vị trí tâm trần nhà và một quả bóng $B$ nằm trên sàn. Chọn hệ trục tọa độ như hình vẽ (đơn vị: m). Biết quả bóng cách tường $(Oxz)$ một khoảng bằng $%s$ m và cách tường $(Oyz)$ một khoảng bằng $%s$ m. Nếu cây quạt trần đột nhiên rơi xuống sàn thì khoảng cách từ vị trí chạm sàn của cây quạt đến quả bóng bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                '}{'
                                '''
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.5}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                        \\clip(-3.6531141859235614,-2.221863460601859) rectangle (9.548958465624983,6.2371014371723215);
                                        \\draw [->,line width=2.pt,color=ffqqqq] (0.,0.) -- (6.,0.);
                                        \\draw [->,line width=2.pt,color=ffqqqq] (0.,0.) -- (0.,4.);
                                        \\draw [->,line width=2.pt,color=ffqqqq] (0.,0.) -- (-3.,-2.);
                                        \\draw [line width=1.pt] (0.,4.)-- (6.,4.);
                                        \\draw [line width=1.pt] (6.,4.)-- (6.,0.);
                                        \\draw [line width=1.pt] (6.,0.)-- (9.,-2.);
                                        \\draw [line width=1.pt] (9.,-2.)-- (-3.,-2.);
                                        \\draw [line width=1.pt] (0.,4.)-- (-3.,6.);
                                        \\draw [line width=1.pt] (-3.,6.)-- (-3.,-2.);
                                        \\draw [line width=1.pt] (-3.,6.)-- (9.,6.);
                                        \\draw [line width=1.pt] (9.,6.)-- (6.,4.);
                                        \\draw [line width=1.pt] (9.,6.)-- (9.,-2.);
                                        \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (3.,5.)-- (2.998925987062749,4.524938136502223);
                                        \\draw [shift={(2.9739456968744564,5.1739456968744575)},line width=1.pt]  plot[domain=2.9929138422963466:4.86106779167814,variable=\\t]({1.*0.17588613411095827*cos(\\t r)+0.*0.17588613411095827*sin(\\t r)},{0.*0.17588613411095827*cos(\\t r)+1.*0.17588613411095827*sin(\\t r)});
                                        \\draw [shift={(3.023390704897584,5.176609295102417)},line width=1.pt]  plot[domain=-1.7024731983419006:0.13167687154699953,variable=\\t]({1.*0.17815153154597965*cos(\\t r)+0.*0.17815153154597965*sin(\\t r)},{0.*0.17815153154597965*cos(\\t r)+1.*0.17815153154597965*sin(\\t r)});
                                        \\draw [shift={(3.,4.929151754397638)},line width=1.pt]  plot[domain=0.9347471348919505:2.206845518697843,variable=\\t]({1.*0.33668794475875985*cos(\\t r)+0.*0.33668794475875985*sin(\\t r)},{0.*0.33668794475875985*cos(\\t r)+1.*0.33668794475875985*sin(\\t r)});
                                        \\draw [shift={(3.,3.7105076527972227)},line width=1.pt]  plot[domain=1.3226885051544013:1.8189041484353898,variable=\\t]({1.*0.8144311918705903*cos(\\t r)+0.*0.8144311918705903*sin(\\t r)},{0.*0.8144311918705903*cos(\\t r)+1.*0.8144311918705903*sin(\\t r)});
                                        \\draw [line width=1.pt] (2.8,4.5)-- (2.8022789107748594,4.559052494920677);
                                        \\draw [line width=1.pt] (3.2,4.5)-- (3.200320379705827,4.557743147983404);
                                        \\draw [shift={(2.999802117544828,4.103149402015884)},line width=1.pt]  plot[domain=1.1553738408372702:1.9796398891134095,variable=\\t]({1.*0.4968531446341548*cos(\\t r)+0.*0.4968531446341548*sin(\\t r)},{0.*0.4968531446341548*cos(\\t r)+1.*0.4968531446341548*sin(\\t r)});
                                        \\draw [shift={(2.998191882600159,4.486300834243774)},line width=1.pt]  plot[domain=0.5738536434273012:2.57614417495839,variable=\\t]({1.*0.17118546867670917*cos(\\t r)+0.*0.17118546867670917*sin(\\t r)},{0.*0.17118546867670917*cos(\\t r)+1.*0.17118546867670917*sin(\\t r)});
                                        \\draw [shift={(2.2146943344202787,4.893111178184815)},line width=1.pt]  plot[domain=-0.33728412111897565:0.13953877589396388,variable=\\t]({1.*0.7566022064468323*cos(\\t r)+0.*0.7566022064468323*sin(\\t r)},{0.*0.7566022064468323*cos(\\t r)+1.*0.7566022064468323*sin(\\t r)});
                                        \\draw [shift={(3.6592511102357257,4.891175628073955)},line width=1.pt]  plot[domain=2.971001730357863:3.5529868415059163,variable=\\t]({1.*0.6339789793005177*cos(\\t r)+0.*0.6339789793005177*sin(\\t r)},{0.*0.6339789793005177*cos(\\t r)+1.*0.6339789793005177*sin(\\t r)});
                                        \\draw [shift={(3.,4.870162041368532)},line width=1.pt]  plot[domain=4.310192063497749:5.114585897271632,variable=\\t]({1.*0.5109328186208291*cos(\\t r)+0.*0.5109328186208291*sin(\\t r)},{0.*0.5109328186208291*cos(\\t r)+1.*0.5109328186208291*sin(\\t r)});
                                        \\draw [shift={(2.8084488025039875,4.45)},line width=1.pt]  plot[domain=1.7381911269151473:4.544994180264439,variable=\\t]({1.*0.05070879868180049*cos(\\t r)+0.*0.05070879868180049*sin(\\t r)},{0.*0.05070879868180049*cos(\\t r)+1.*0.05070879868180049*sin(\\t r)});
                                        \\draw [shift={(3.1888726681701747,4.45)},line width=1.pt]  plot[domain=-1.3518182543521524:1.3518182543521449,variable=\\t]({1.*0.05122321264476625*cos(\\t r)+0.*0.05122321264476625*sin(\\t r)},{0.*0.05122321264476625*cos(\\t r)+1.*0.05122321264476625*sin(\\t r)});
                                        \\draw [line width=1.pt] (3.239897706438489,4.445498557634705)-- (4.6,4.2);
                                        \\draw [line width=1.pt] (3.2,4.4)-- (3.9054445025852242,4.1544739120603085);
                                        \\draw [shift={(4.192103126758628,5.102054969150983)},line width=1.pt]  plot[domain=4.41862534372324:5.137059523503574,variable=\\t]({1.*0.9899914275235263*cos(\\t r)+0.*0.9899914275235263*sin(\\t r)},{0.*0.9899914275235263*cos(\\t r)+1.*0.9899914275235263*sin(\\t r)});
                                        \\draw [line width=1.pt] (3.141956037698796,4.579232703884063)-- (4.006151624581561,5.134431676101583);
                                        \\draw [shift={(3.8070464935932393,4.98696501576708)},line width=1.pt]  plot[domain=-1.0029315256254092:0.6374884041012207,variable=\\t]({1.*0.2477685797192379*cos(\\t r)+0.*0.2477685797192379*sin(\\t r)},{0.*0.2477685797192379*cos(\\t r)+1.*0.2477685797192379*sin(\\t r)});
                                        \\draw [line width=1.pt] (2.7578141935315306,4.447257986513928)-- (1.5388271356713215,4.247434332364619);
                                        \\draw [line width=1.pt] (2.8,4.4)-- (2.0346160439609773,4.181587367982399);
                                        \\draw [shift={(1.8811022387639982,4.925141618722016)},line width=1.pt]  plot[domain=4.244710668442441:4.91598776909766,variable=\\t]({1.*0.7592360714422158*cos(\\t r)+0.*0.7592360714422158*sin(\\t r)},{0.*0.7592360714422158*cos(\\t r)+1.*0.7592360714422158*sin(\\t r)});
                                        \\draw [line width=1.pt] (2.853651707228016,4.5780210740464184)-- (1.9752561105025659,5.096169992942922);
                                        \\draw [line width=1.pt] (2.8022789107748594,4.559052494920677)-- (2.057438270797806,4.750139844331384);
                                        \\draw [shift={(2.132214266518977,4.95067334915599)},line width=1.pt]  plot[domain=2.3940713253713897:4.3554735831018245,variable=\\t]({1.*0.21402134494795927*cos(\\t r)+0.*0.21402134494795927*sin(\\t r)},{0.*0.21402134494795927*cos(\\t r)+1.*0.21402134494795927*sin(\\t r)});
                                        \\draw [line width=1.pt] (3.200320379705827,4.557743147983404)-- (3.940304660199341,4.778083398268392);
                                        \\draw [line width=1.pt] (4.,2.)-- (4.,0.);
                                        \\draw [line width=1.pt] (4.,2.)-- (5.,2.);
                                        \\draw [line width=1.pt] (5.,2.)-- (5.,0.);
                                        \\draw [line width=1.pt] (-1.,3.)-- (-1.,2.);
                                        \\draw [line width=1.pt] (-1.,3.)-- (-1.9734336194285762,3.400648516062183);
                                        \\draw [line width=1.pt] (-1.,2.)-- (-1.9958184070692,1.6210578986325814);
                                        \\draw [line width=1.pt] (-1.9734336194285762,3.400648516062183)-- (-1.9958184070692,1.6210578986325814);
                                        \\draw [line width=1.pt] (0.,-1.) circle (0.366481096667244cm);
                                        \\draw [shift={(-0.08654937765959228,-0.7114432146281321)},line width=1.pt]  plot[domain=3.6960737581972776:5.0037896326070666,variable=\\t]({1.*0.3012570549504342*cos(\\t r)+0.*0.3012570549504342*sin(\\t r)},{0.*0.3012570549504342*cos(\\t r)+1.*0.3012570549504342*sin(\\t r)});
                                        \\draw [shift={(-0.08967514797005294,-0.7577822472595748)},line width=1.pt]  plot[domain=3.8288680190253634:5.318394919301728,variable=\\t]({1.*0.3576908726436746*cos(\\t r)+0.*0.3576908726436746*sin(\\t r)},{0.*0.3576908726436746*cos(\\t r)+1.*0.3576908726436746*sin(\\t r)});
                                        \\draw [shift={(-0.07763404632423303,-0.785780533649937)},line width=1.pt]  plot[domain=4.091904844129493:5.340751207310275,variable=\\t]({1.*0.4439050888508623*cos(\\t r)+0.*0.4439050888508623*sin(\\t r)},{0.*0.4439050888508623*cos(\\t r)+1.*0.4439050888508623*sin(\\t r)});
                                        \\draw [shift={(-0.0568061132697527,-0.8617581808928391)},line width=1.pt]  plot[domain=4.4141578896579485:5.353345806153803,variable=\\t]({1.*0.4694240876479999*cos(\\t r)+0.*0.4694240876479999*sin(\\t r)},{0.*0.4694240876479999*cos(\\t r)+1.*0.4694240876479999*sin(\\t r)});
                                        \\draw [shift={(-0.06631444829637542,-1.3034575516351758)},line width=1.pt]  plot[domain=0.09372743880501015:1.3556490004635815,variable=\\t]({1.*0.31061888496559265*cos(\\t r)+0.*0.31061888496559265*sin(\\t r)},{0.*0.31061888496559265*cos(\\t r)+1.*0.31061888496559265*sin(\\t r)});
                                        \\draw [shift={(0.4439467921537017,-1.0461722114592478)},line width=1.pt]  plot[domain=2.1918710941116375:3.037961304834571,variable=\\t]({1.*0.44634137985918304*cos(\\t r)+0.*0.44634137985918304*sin(\\t r)},{0.*0.44634137985918304*cos(\\t r)+1.*0.44634137985918304*sin(\\t r)});
                                        \\draw [shift={(-0.02269781042143554,-1.2200076207602657)},line width=1.pt]  plot[domain=0.09774506397630472:1.4208899176057748,variable=\\t]({1.*0.33957830144517137*cos(\\t r)+0.*0.33957830144517137*sin(\\t r)},{0.*0.33957830144517137*cos(\\t r)+1.*0.33957830144517137*sin(\\t r)});
                                        \\draw [shift={(0.05224423968539891,-1.146827057401347)},line width=1.pt]  plot[domain=0.3874697695364513:1.5292791092644813,variable=\\t]({1.*0.33887677053483684*cos(\\t r)+0.*0.33887677053483684*sin(\\t r)},{0.*0.33887677053483684*cos(\\t r)+1.*0.33887677053483684*sin(\\t r)});
                                        \\draw [shift={(-0.31721854896698526,-1.9158826908667288)},line width=1.pt]  plot[domain=1.052902036501407:1.2086976078999037,variable=\\t]({1.*1.2732838784276181*cos(\\t r)+0.*1.2732838784276181*sin(\\t r)},{0.*1.2732838784276181*cos(\\t r)+1.*1.2732838784276181*sin(\\t r)});
                                        \\draw [shift={(0.3932169058625533,-1.0320245652426867)},line width=1.pt]  plot[domain=2.250322685945808:3.101541762308592,variable=\\t]({1.*0.5014896626416789*cos(\\t r)+0.*0.5014896626416789*sin(\\t r)},{0.*0.5014896626416789*cos(\\t r)+1.*0.5014896626416789*sin(\\t r)});
                                        \\draw [shift={(0.2405866805797878,-1.001029729741785)},line width=1.pt]  plot[domain=2.2541677166888734:3.091913217645783,variable=\\t]({1.*0.4685318583795698*cos(\\t r)+0.*0.4685318583795698*sin(\\t r)},{0.*0.4685318583795698*cos(\\t r)+1.*0.4685318583795698*sin(\\t r)});
                                        \\draw [shift={(0.027040528223003953,-0.9298375635846504)},line width=1.pt]  plot[domain=2.3942272924740786:3.1095691259316305,variable=\\t]({1.*0.331908109324021*cos(\\t r)+0.*0.331908109324021*sin(\\t r)},{0.*0.331908109324021*cos(\\t r)+1.*0.331908109324021*sin(\\t r)});
                                        \\draw [line width=1.pt] (3.90278522781591,2.093015500517575)-- (3.90810375489556,0.);
                                        \\draw [line width=1.pt] (3.90278522781591,2.093015500517575)-- (5.072861185338929,2.0876969734379247);
                                        \\draw [line width=1.pt] (5.072861185338929,2.0876969734379247)-- (5.088816766577879,0.);
                                        \\draw (0,0.5) node [below left] {$O$}; 
                                        \\draw (6,0) node [below left] {$y$};
                                        \\draw (0,4) node [below left] {$z$};
                                        \\draw (-2.5,-1.2) node [below left] {$x$}; 
                                        \\draw (3,0) node [below left] {$%s$ m};
                                \\end{tikzpicture} }
                                '''
                                '}'
                                %(latex(a),latex(b),latex(c),latex(d),latex(e),
                                latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (
                            'Căn phòng có chiều dài $%s$ m, chiều rộng $%s$ m và cao $%s$ m. \\\\ \n'
                            'Cây quạt trần $A$ nằm ở vị trí tâm trần nhà. Do đó, tọa độ của cây quạt trần $A$ là $A \\left( \\dfrac{%s}{2}; \\dfrac{%s}{2}; %s \\right)$ hay $A(%s;%s;%s)$. \\\\ \n'
                            'Quả bóng nằm trên sàn, cách tường $(Oxz)$ $%s$ m, tức là tung độ $y=%s$. \\\\ \n'
                            'Quả bóng cũng cách tường $(Oyz)$ $%s$ m, tức là hoành độ $x=%s$. \\\\ \n'
                            'Quả bóng nằm trên sàn nhà nên cao độ bằng $z=0$ \\\\ \n'
                            'Suy ra tọa độ của bóng là $B(%s;%s;0)$ \\\\ \n'
                            'Khi cây quạt rơi xuống sàn, vị trí chạm sàn của cây quạt sẽ có cùng hoành độ $x$ và tung độ $y$ như tọa độ của cây quạt khi ở trên trần, chỉ có cao độ $z$ thay đổi thành $0$ (vì nằm trên sàn) (tức là hình chiếu vuông góc của điểm $A$ lên mặt phẳng $(Oxy)$).\\\\ \n'
                            'Vị trí chạm sàn của cây quạt có tọa độ là $A\'(%s;%s;0)$.\\\\ \n'
                            'Ta có $\\vec{A\'B}=(%s; %s; 0)$. \\\\ \n'
                            'Vậy khoảng cách từ vị trí chạm sàn của cây quạt đến quả bóng là $%s \\approx %s$ m.'
                        %(latex(a),latex(b),latex(c),
                            latex(b),latex(a),latex(c),
                            latex(Rational(b,2)),latex(Rational(a,2)),latex(c),
                            latex(d),latex(d),
                            latex(e),latex(e),
                            latex(e),latex(d),
                            latex(Rational(b,2)),latex(Rational(a,2)),
                            latex(e-Rational(b,2)),latex(d-Rational(a,2)),
                            latex(kc),latex(kq)

                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(kq)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


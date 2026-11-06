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


def bt_dang3_p4_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,13)
                x0=a*(2+sqrt(3))*2
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('Cho tam giác ${O A_1 A_2}$ vuông tại ${A_2, A_1 A_2=%s}$ và ${\\widehat{A_1 O A_2}=30^{\\circ}}$$zz$\\\\ \n'
                                ' Hạ các đường vuông góc ${A_2 A_3 \\perp O A_1 ; A_3 A_4 \\perp O A_2 ; A_4 A_5 \\perp O A_1 ; \\ldots}$ '
                                'Tiếp tục quá trình này, ta nhận được đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ '
                                'Tính độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Các góc ${\\widehat{A_1 A_2 A_3}, \\widehat{A_2 A_3 A_4}, \\widehat{A_3 A_4 A_5}, \\ldots}$ đều bằng góc ${\\widehat{A_1 O A_2}}$ nên đều có số đo ${30^{\\circ}}$$zz$\\\\ \n'
                    '$ A_2 A_3=A_1 A_2 \\cdot \\cos 30^{\\circ}=%s \\cdot \\dfrac{\\sqrt{3}}{2}$$zz$ \\\\ \n'
                        '$ A_3 A_4=A_2 A_3 \\cdot \\cos 30^{\\circ}=%s \\cdot \\dfrac{\\sqrt{3}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}=%s\\left(\\frac{\\sqrt{3}}{2}\\right)^2 ;$ \\\\ \n'
                            '$ A_4 A_5=A_3 A_4 \\cdot \\cos 30^{\\circ}=%s\\left(\\frac{\\sqrt{3}}{2}\\right)^2 \\cdot \\dfrac{\\sqrt{3}}{2}=%s\\left(\\dfrac{\\sqrt{3}}{2}\\right)^3 ; \\ldots$\\\\ \n'
                            'Vậy độ dài các đoạn thẳng ${A_1 A_2, A_2 A_3, A_3 A_4, \\ldots}$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu bằng $%s$ và công bội bằng ${\\dfrac{\\sqrt{3}}{2}}$$zz$\\\\ \n'
                            'Từ đó, độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ là\\\\ \n'
                            '${l=%s \\cdot \\dfrac{1}{1-\\dfrac{\\sqrt{3}}{2}}=\\dfrac{%s}{2-\\sqrt{3}}=\\dfrac{%s (2+\\sqrt{3})}{2^2-(\\sqrt{3})^2}=%s(2+\\sqrt{3})}\\approx %s$$zz$'
                            %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a*2),latex(a*2),latex(a*2),latex(kq),)
                            )
                hinhve=('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm]
                \\clip(-2$zz$7688503419443182,-0$zz$8) rectangle (15$zz$950239884793666,4$zz$6);
                \\draw (0,0)-- (7,0);
                \\draw (7,4)-- (0,0);
                \\draw (7,4)-- (7,0);
                \\draw (5$zz$276923076923077,3$zz$0153846153846153)-- (7,0);
                \\draw (5$zz$276923076923077,0)-- (5$zz$276923076923077,3$zz$0153846153846153);
                \\draw (3$zz$977988165680473,2$zz$2731360946745562)-- (5$zz$276923076923077,0);
                \\draw (3$zz$977988165680473,0)-- (3$zz$977988165680473,2$zz$2731360946745562);
                \\draw (7,0$zz$4)-- (6$zz$6,0$zz$4);
                \\draw (6$zz$6,0$zz$4)-- (6$zz$6,0);
                \\draw (5$zz$496814779546399,3$zz$141037016883656)-- (5$zz$647879233199747,2$zz$9258738513245564);
                \\draw (5$zz$647879233199747,2$zz$9258738513245564)-- (5$zz$411006254174768,2$zz$7807390551941555);
                \\draw (5$zz$276923076923077,0$zz$3009796844740978)-- (5,0$zz$3);
                \\draw (5,0$zz$3)-- (5,0);
                \\draw (4$zz$074634946382184,2$zz$1040042284465623)-- (4$zz$2644563519572385,2$zz$2055474375400426);
                \\draw (4$zz$2644563519572385,2$zz$2055474375400426)-- (4$zz$160910044832849,2$zz$377662882761628);
                \\draw (3$zz$977988165680473,0$zz$25128396978831574)-- (3$zz$7,0$zz$25);
                \\draw (3$zz$7,0$zz$25)-- (3$zz$7,0);
                \\draw [shift={(0$zz$5081491099148285,0$zz$14269847452376205)}] plot[domain=-1$zz$5098729208342467:1$zz$6317197327555462,variable=\\t]({1$zz$*0$zz$14296370890972296*cos(\\t r)+0$zz$*0$zz$14296370890972296*sin(\\t r)},{0$zz$*0$zz$14296370890972296*cos(\\t r)+1$zz$*0$zz$14296370890972296*sin(\\t r)});
                \\draw (6$zz$894121420985264,4$zz$504982342117207) node[anchor=north west] {$A1$};
                \\draw (5$zz$050221012117059,3$zz$7) node[anchor=north west] {$A3$};
                \\draw (3$zz$591439043075757,2$zz$9) node[anchor=north west] {$A5$};
                \\draw (-0$zz$5748422605062006,0$zz$33870103853523803) node[anchor=north west] {$O$};
                \\draw (0$zz$8839397085351011,0$zz$5020846190678642) node[anchor=north west] {$30^{\\circ}$};
                \\draw (3$zz$731482112103722,0$zz$05861490047930736) node[anchor=north west] {$A6$};
                \\draw (5$zz$050221012117059,0$zz$0936256677362987) node[anchor=north west] {$A4$};
                \\draw (6$zz$987483467003907,0$zz$07028515623163781) node[anchor=north west] {$A2$};
                \\draw (2$zz$937904720945254,1$zz$1206081739413778) node[anchor=north west] {$\\cdots$};
            \\end{tikzpicture}
                \\end{center}''')
                #Đáp án


            if dang=='2':
                # Khai báo biến
                a=randint(2,28)
                x0=a*(2+sqrt(2))
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('Cho tam giác ${O A_1 A_2}$ vuông tại ${A_2, A_1 A_2=%s}$ và ${\\widehat{A_1 O A_2}=45^{\\circ}}$$zz$\\\\ \n'
                                ' Hạ các đường vuông góc ${A_2 A_3 \\perp O A_1 ; A_3 A_4 \\perp O A_2 ; A_4 A_5 \\perp O A_1 ; \\ldots}$ '
                                'Tiếp tục quá trình này, ta nhận được đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ '
                                'Tính độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Các góc ${\\widehat{A_1 A_2 A_3}, \\widehat{A_2 A_3 A_4}, \\widehat{A_3 A_4 A_5}, \\ldots}$ đều bằng góc ${\\widehat{A_1 O A_2}}$ nên đều có số đo ${45^{\\circ}}$$zz$\\\\ \n'
                    '$ A_2 A_3=A_1 A_2 \\cdot \\cos 45^{\\circ}=%s \\cdot \\dfrac{\\sqrt{2}}{2}$$zz$ \\\\ \n'
                        '$ A_3 A_4=A_2 A_3 \\cdot \\cos 45^{\\circ}=%s \\cdot \\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{2}}{2}=%s\\left(\\frac{\\sqrt{2}}{2}\\right)^2 ;$ \\\\ \n'
                            '$ A_4 A_5=A_3 A_4 \\cdot \\cos 45^{\\circ}=%s\\left(\\frac{\\sqrt{2}}{2}\\right)^2 \\cdot \\dfrac{\\sqrt{2}}{2}=%s\\left(\\dfrac{\\sqrt{2}}{2}\\right)^3 ; \\ldots$\\\\ \n'
                            'Vậy độ dài các đoạn thẳng ${A_1 A_2, A_2 A_3, A_3 A_4, \\ldots}$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu bằng $%s$ và công bội bằng ${\\dfrac{\\sqrt{2}}{2}}$$zz$\\\\ \n'
                            'Từ đó, độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ là\\\\ \n'
                            '${l=%s \\cdot \\dfrac{1}{1-\\dfrac{\\sqrt{2}}{2}}=\\dfrac{%s }{2-\\sqrt{2}}=\\dfrac{%s (2+\\sqrt{2})}{2^2-(\\sqrt{2})^2}=\\dfrac{%s(2+\\sqrt{2})}{2}}\\approx %s$$zz$'
                            %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a*2),latex(a*2),latex(a*2),latex(kq),)
                            )
                hinhve=('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm]
                \\clip(-2$zz$7688503419443182,-0$zz$8) rectangle (15$zz$950239884793666,4$zz$6);
                \\draw (0,0)-- (7,0);
                \\draw (7,4)-- (0,0);
                \\draw (7,4)-- (7,0);
                \\draw (5$zz$276923076923077,3$zz$0153846153846153)-- (7,0);
                \\draw (5$zz$276923076923077,0)-- (5$zz$276923076923077,3$zz$0153846153846153);
                \\draw (3$zz$977988165680473,2$zz$2731360946745562)-- (5$zz$276923076923077,0);
                \\draw (3$zz$977988165680473,0)-- (3$zz$977988165680473,2$zz$2731360946745562);
                \\draw (7,0$zz$4)-- (6$zz$6,0$zz$4);
                \\draw (6$zz$6,0$zz$4)-- (6$zz$6,0);
                \\draw (5$zz$496814779546399,3$zz$141037016883656)-- (5$zz$647879233199747,2$zz$9258738513245564);
                \\draw (5$zz$647879233199747,2$zz$9258738513245564)-- (5$zz$411006254174768,2$zz$7807390551941555);
                \\draw (5$zz$276923076923077,0$zz$3009796844740978)-- (5,0$zz$3);
                \\draw (5,0$zz$3)-- (5,0);
                \\draw (4$zz$074634946382184,2$zz$1040042284465623)-- (4$zz$2644563519572385,2$zz$2055474375400426);
                \\draw (4$zz$2644563519572385,2$zz$2055474375400426)-- (4$zz$160910044832849,2$zz$377662882761628);
                \\draw (3$zz$977988165680473,0$zz$25128396978831574)-- (3$zz$7,0$zz$25);
                \\draw (3$zz$7,0$zz$25)-- (3$zz$7,0);
                \\draw [shift={(0$zz$5081491099148285,0$zz$14269847452376205)}] plot[domain=-1$zz$5098729208342467:1$zz$6317197327555462,variable=\\t]({1$zz$*0$zz$14296370890972296*cos(\\t r)+0$zz$*0$zz$14296370890972296*sin(\\t r)},{0$zz$*0$zz$14296370890972296*cos(\\t r)+1$zz$*0$zz$14296370890972296*sin(\\t r)});
                \\draw (6$zz$894121420985264,4$zz$504982342117207) node[anchor=north west] {$A1$};
                \\draw (5$zz$050221012117059,3$zz$7) node[anchor=north west] {$A3$};
                \\draw (3$zz$591439043075757,2$zz$9) node[anchor=north west] {$A5$};
                \\draw (-0$zz$5748422605062006,0$zz$33870103853523803) node[anchor=north west] {$O$};
                \\draw (0$zz$8839397085351011,0$zz$5020846190678642) node[anchor=north west] {$45^{\\circ}$};
                \\draw (3$zz$731482112103722,0$zz$05861490047930736) node[anchor=north west] {$A6$};
                \\draw (5$zz$050221012117059,0$zz$0936256677362987) node[anchor=north west] {$A4$};
                \\draw (6$zz$987483467003907,0$zz$07028515623163781) node[anchor=north west] {$A2$};
                \\draw (2$zz$937904720945254,1$zz$1206081739413778) node[anchor=north west] {$\\cdots$};
            \\end{tikzpicture}
                \\end{center}''')
                #Đáp án


            if dang=='3':
                # Khai báo biến
                a=randint(2,49)
                x0=a*(2+2*sqrt(2))/2
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('Cho tam giác ${O A_1 A_2}$ vuông tại ${A_2, A_1 A_2=%s}$ và ${\\widehat{A_1 O A_2}=60^{\\circ}}$$zz$\\\\ \n'
                                ' Hạ các đường vuông góc ${A_2 A_3 \\perp O A_1 ; A_3 A_4 \\perp O A_2 ; A_4 A_5 \\perp O A_1 ; \\ldots}$ '
                                'Tiếp tục quá trình này, ta nhận được đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ '
                                'Tính độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$$zz$'
                                %(latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Các góc ${\\widehat{A_1 A_2 A_3}, \\widehat{A_2 A_3 A_4}, \\widehat{A_3 A_4 A_5}, \\ldots}$ đều bằng góc ${\\widehat{A_1 O A_2}}$ nên đều có số đo ${60^{\\circ}}$$zz$\\\\ \n'
                    '$ A_2 A_3=A_1 A_2 \\cdot \\cos 60^{\\circ}=%s \\cdot \\dfrac{1}{2}$$zz$ \\\\ \n'
                        '$ A_3 A_4=A_2 A_3 \\cdot \\cos 60^{\\circ}=%s \\cdot \\dfrac{1}{2} \\cdot \\dfrac{1}{2}=%s\\left(\\frac{1}{2}\\right)^2 ;$ \\\\ \n'
                            '$ A_4 A_5=A_3 A_4 \\cdot \\cos 60^{\\circ}=%s\\left(\\frac{1}{2}\\right)^2 \\cdot \\dfrac{1}{2}=%s\\left(\\dfrac{1}{2}\\right)^3 ; \\ldots$\\\\ \n'
                            'Vậy độ dài các đoạn thẳng ${A_1 A_2, A_2 A_3, A_3 A_4, \\ldots}$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu bằng $%s$ và công bội bằng ${\\dfrac{1}{2}}$$zz$\\\\ \n'
                            'Từ đó, độ dài đường gấp khúc ${A_1 A_2 A_3 A_4 \\ldots}$ là\\\\ \n'
                            '${l=%s\\cdot \\dfrac{1}{1-\\dfrac{1}{2}}=%s\\cdot 2= %s}$$zz$'
                            %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(2*a),)
                            )
                hinhve=('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm]
                \\clip(-2$zz$7688503419443182,-0$zz$8) rectangle (15$zz$950239884793666,4$zz$6);
                \\draw (0,0)-- (7,0);
                \\draw (7,4)-- (0,0);
                \\draw (7,4)-- (7,0);
                \\draw (5$zz$276923076923077,3$zz$0153846153846153)-- (7,0);
                \\draw (5$zz$276923076923077,0)-- (5$zz$276923076923077,3$zz$0153846153846153);
                \\draw (3$zz$977988165680473,2$zz$2731360946745562)-- (5$zz$276923076923077,0);
                \\draw (3$zz$977988165680473,0)-- (3$zz$977988165680473,2$zz$2731360946745562);
                \\draw (7,0$zz$4)-- (6$zz$6,0$zz$4);
                \\draw (6$zz$6,0$zz$4)-- (6$zz$6,0);
                \\draw (5$zz$496814779546399,3$zz$141037016883656)-- (5$zz$647879233199747,2$zz$9258738513245564);
                \\draw (5$zz$647879233199747,2$zz$9258738513245564)-- (5$zz$411006254174768,2$zz$7807390551941555);
                \\draw (5$zz$276923076923077,0$zz$3009796844740978)-- (5,0$zz$3);
                \\draw (5,0$zz$3)-- (5,0);
                \\draw (4$zz$074634946382184,2$zz$1040042284465623)-- (4$zz$2644563519572385,2$zz$2055474375400426);
                \\draw (4$zz$2644563519572385,2$zz$2055474375400426)-- (4$zz$160910044832849,2$zz$377662882761628);
                \\draw (3$zz$977988165680473,0$zz$25128396978831574)-- (3$zz$7,0$zz$25);
                \\draw (3$zz$7,0$zz$25)-- (3$zz$7,0);
                \\draw [shift={(0$zz$5081491099148285,0$zz$14269847452376205)}] plot[domain=-1$zz$5098729208342467:1$zz$6317197327555462,variable=\\t]({1$zz$*0$zz$14296370890972296*cos(\\t r)+0$zz$*0$zz$14296370890972296*sin(\\t r)},{0$zz$*0$zz$14296370890972296*cos(\\t r)+1$zz$*0$zz$14296370890972296*sin(\\t r)});
                \\draw (6$zz$894121420985264,4$zz$504982342117207) node[anchor=north west] {$A1$};
                \\draw (5$zz$050221012117059,3$zz$7) node[anchor=north west] {$A3$};
                \\draw (3$zz$591439043075757,2$zz$9) node[anchor=north west] {$A5$};
                \\draw (-0$zz$5748422605062006,0$zz$33870103853523803) node[anchor=north west] {$O$};
                \\draw (0$zz$8839397085351011,0$zz$5020846190678642) node[anchor=north west] {$60^{\\circ}$};
                \\draw (3$zz$731482112103722,0$zz$05861490047930736) node[anchor=north west] {$A6$};
                \\draw (5$zz$050221012117059,0$zz$0936256677362987) node[anchor=north west] {$A4$};
                \\draw (6$zz$987483467003907,0$zz$07028515623163781) node[anchor=north west] {$A2$};
                \\draw (2$zz$937904720945254,1$zz$1206081739413778) node[anchor=north west] {$\\cdots$};
            \\end{tikzpicture}
                \\end{center}''')
                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(hinhve)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('+-', '-').replace('1a', 'a').replace('1b', 'b')
            return content    


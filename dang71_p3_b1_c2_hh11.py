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


def bt_dang71_p3_b1_c2_hh11(self):
            # Khai báo biến
            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Random cạnh a từ 2 đến 10 để tránh số quá nhỏ
            val_a = random.randint(2, 6) 
            # Tỉ lệ AD = k*a. Ở đề gốc k=2.
            k = random.randint(2, 3)
            # Tỉ lệ AB = n*AH. Ở đề gốc n=3.
            n = random.randint(2, 4)

            # Tính toán các thông số theo a
            # AB = a, AD = k*a
            # S_SAB = a^2 => 1/2 * SH * AB = a^2 => SH = 2*a
            sh_val = 2 * val_a
            ah_val = Rational(val_a, n)
            ad_val = k * val_a

            # Tính SA^2 = SH^2 + AH^2
            sa_sq = sh_val**2 + ah_val**2
            sa = sqrt(sa_sq)

            # Tính AE (E là điểm sao cho ADBE là hbh => AE = BD)
            # BD^2 = AB^2 + AD^2
            ae_sq = val_a**2 + ad_val**2
            ae = sqrt(ae_sq)

            # Tính BE = AD (tính chất hình bình hành)
            be_val = ad_val

            # Tính SE^2 dùng định lý cos hoặc tọa độ. 
            # Ở đây dùng tam giác vuông SHE (với H là hình chiếu S lên AB)
            # Trong mp(ABCD), tính HE^2. 
            # Gọi tọa độ H(val_a/n, 0), A(0,0), B(val_a, 0), D(0, ad_val), E(val_a, ad_val)
            # HE^2 = (xE - xH)^2 + (yE - yH)^2
            he_sq = (val_a - ah_val)**2 + ad_val**2
            se_sq = sh_val**2 + he_sq
            se = sqrt(se_sq)

            # Tính cos(SA, AE) = | (SA^2 + AE^2 - SE^2) / (2 * SA * AE) |
            tu_so = sa_sq + ae_sq - se_sq
            mau_so = 2 * sa * ae
            cos_val = abs(tu_so / mau_so)

            # --- B2: Viết lại nội dung bài toán ---

            # Câu hỏi
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật, $AB = %s, AD = %s$. Hình chiếu vuông góc của $S$ xuống mặt phẳng $(ABCD)$ là điểm $H$ thuộc $AB$ sao cho $AB = %s AH$. Biết $S_{\triangle SAB} = %s$. Giá trị $\cos(SA; BD)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                            % (latex(val_a), latex(ad_val), latex(n), latex(val_a**2)))

            # Đáp án đúng
            da_dung = '$%s$' % latex(cos_val)

            # Tạo các đáp án nhiễu (random một vài giá trị phân số đơn giản)
            s = []
            while len(s) < 3:
                fake_num = random.randint(1, 20)
                fake_den = random.randint(10, 50)
                fake_val = '$%s$' % latex(Rational(fake_num, fake_den))
                if fake_val != da_dung and fake_val not in s:
                    s.append(fake_val)

            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # Trộn đáp án
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            h1=cos_val
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            loigiai = ('\\begin{center}'
                       '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.8cm,y=0.8cm]
            	\\clip(-4.9,-2.86) rectangle (6.28,3.7);
            	\\draw [dash pattern=on 2pt off 2pt] (1.,3.)-- (1.,0.);
            	\\draw [dash pattern=on 2pt off 2pt] (1.,0.)-- (5.,0.);
            	\\draw (5.,0.)-- (4.,-2.);
            	\\draw (4.,-2.)-- (0.,-2.);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,-2.)-- (1.,0.);
            	\\draw (1.,3.)-- (-4.,-2.);
            	\\draw (-4.,-2.)-- (0.,-2.);
            	\\draw (0.,-2.)-- (1.,3.);
            	\\draw (1.,3.)-- (4.,-2.);
            	\\draw (1.,3.)-- (5.,0.);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,-2.)-- (3.,0.);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,-2.)-- (5.,0.);
            	\\draw [dash pattern=on 2pt off 2pt] (1.,3.)-- (0.664,-0.672);
            	\\draw [dash pattern=on 2pt off 2pt] (-4.,-2.)-- (1.,0.);
            	\\draw (0.76,3.84) node[anchor=north west] {$S$};
            	\\draw (1.1,0.7) node[anchor=north west] {$A$};
            	\\draw (-0.28,-2) node[anchor=north west] {$B$};
            	\\draw (3.76,-2) node[anchor=north west] {$C$};
            	\\draw (5,0.5) node[anchor=north west] {$D$};
            	\\draw (2.9,0.7) node[anchor=north west] {$M$};
            	\\draw (0.76,-0.18) node[anchor=north west] {$H$};
            	\\draw (-4.5,-2) node[anchor=north west] {$E$};
            \\end{tikzpicture}'''
            '\\end{center}'
                r'''Gọi $E$ là điểm sao cho $ADBE$ là hình bình hành $\Rightarrow AE \parallel BD \Rightarrow (SA; BD) = (SA; AE)$. \\
                       Ta có $AE = BD = \sqrt{AB^2 + AD^2} = %s$. \\
                       $S_{\triangle SAB} = \frac{1}{2}SH \cdot AB = %s^2 \Rightarrow SH = %s$. \\
                       $AH = \frac{1}{%s}AB = %s$. \\
                       Xét tam giác vuông $SHA$: $SA = \sqrt{SH^2 + AH^2} = %s$. \\
                       Xét tam giác vuông $SHE$ (với $HE^2 = HB^2 + BE^2$): $SE = \sqrt{SH^2 + HB^2 + BE^2} = %s$. \\
                       Áp dụng định lý hàm số cos trong tam giác $SAE$: \\
                       $\cos \widehat{SAE} = \frac{SA^2 + AE^2 - SE^2}{2 \cdot SA \cdot AE} = %s$. \\
                       Vậy $\cos(SA; BD) = %s \approx %s$.'''
                       % (latex(ae), latex(val_a), latex(sh_val), latex(n), latex(ah_val), 
                          latex(sa), latex(se), latex(tu_so/mau_so), latex(cos_val),str(kqz)))

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


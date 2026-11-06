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


def bt_dang52_p3_b6_c2_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        val_AB = randint(3, 9)
        val_AD = randint(4, 10)
        k = randint(1, 4)
        val_SA = 3 * k * 3  # bội số của 9 để V nguyên đẹp

        V_total = Rational(1, 3) * val_SA * val_AB * val_AD
        V_tren = Rational(1, 3) * V_total
        V_can_tim = V_total - V_tren

        number = Decimal(str(float(V_can_tim)))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP) if V_can_tim % 1 == 0 else number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # TikZ code vẽ hình chính xác 100% theo mẫu và quy cách
        tikz_code = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "    \\coordinate (A) at (0,0);\n"
            "    \\coordinate (B) at (-1.5,-2);\n"
            "    \\coordinate (C) at (3,-2);\n"
            "    \\coordinate (D) at (4.5,0);\n"
            "    \\coordinate (S) at (0,4.2);\n"
            "    \\coordinate (O) at (intersection of A--C and B--D);\n"
            "    \\coordinate (M) at ($(S)!0.6667!(B)$);\n"
            "    \\coordinate (N) at ($(S)!0.6667!(D)$);\n"
            "    \\coordinate (I) at (intersection of S--O and M--N);\n"
            "    \\coordinate (P) at ($(S)!0.5!(C)$);\n"
            "    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S) (S)--(C) (M)--(P)--(N);\n"
            "    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(M) (A)--(N) (A)--(P) (M)--(N);\n"
            "    \\draw[line width=0.8pt] (0,0.3) -- (0.3,0.3) -- (0.3,0);\n"
            "    \\fill (A) circle (1pt) node[below] {$A$};\n"
            "    \\fill (B) circle (1pt) node[below left] {$B$};\n"
            "    \\fill (C) circle (1pt) node[below right] {$C$};\n"
            "    \\fill (D) circle (1pt) node[right] {$D$};\n"
            "    \\fill (S) circle (1pt) node[above] {$S$};\n"
            "    \\fill (O) circle (1pt) node[below] {$O$};\n"
            "    \\fill (M) circle (1pt) node[left] {$M$};\n"
            "    \\fill (N) circle (1pt) node[right] {$N$};\n"
            "    \\fill (P) circle (1pt) node[above] {$P$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = (
            '''\\immini{Một trung tâm triển lãm kiến trúc thiết kế một mô hình tòa nhà kính có dạng hình chóp $S.ABCD$ với đáy $ABCD$ là hình chữ nhật có $AB=%s\\text{ m}$, $AD=%s\\text{ m}$. Cột trụ chính $SA$ vuông góc với mặt phẳng đáy $(ABCD)$ và có chiều cao $SA=%s\\text{ m}$. Để lắp đặt hệ thống tấm năng lượng mặt trời và chia không gian lấy sáng, kiến trúc sư cho cắt khối chóp $S.ABCD$ bởi mặt phẳng $(\\alpha)$ đi qua đỉnh $A$ và song song với đường chéo $BD$. Mặt phẳng $(\\alpha)$ cắt cạnh $SB$ tại $M$ sao cho $SM=2MB$, cắt cạnh $SD$ tại $N$ và cắt cạnh $SC$ tại $P$. Tính thể tích $V$ của phần không gian bên dưới mặt phẳng $(\\alpha)$ thuộc mô hình tòa nhà kính (chính là thể tích khối đa diện $ABCDMNP$).}
            {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\tikzset {_imctskfsg/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            	\\pgfdeclarehorizontalshading{_omx9v3ji0}{150bp}{rgb(0bp)=(0.6,0.85,1);
            		rgb(37.5bp)=(0.6,0.85,1);
            		rgb(62.5bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\\tikzset {_oohkxqtiz/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            	\\pgfdeclarehorizontalshading{_312cu86ph}{150bp}{rgb(0bp)=(0.6,0.85,1);
            		rgb(37.5bp)=(0.6,0.85,1);
            		rgb(62.5bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\\tikzset{every picture/.style={line width=0.75pt}}  
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (266.62,144.19) -- (71.33,193.13) -- (70.6,131.9) -- cycle ;
            	\\path  [shading=_omx9v3ji0,_imctskfsg] (141.76,43.47) -- (221.67,194.13) -- (71.33,193.13) -- cycle ; 
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ] (141.76,43.47) -- (221.67,194.13) -- (71.33,193.13) -- cycle ; 
            	\\path  [shading=_312cu86ph,_oohkxqtiz] (141.76,43.47) -- (266.62,144.19) -- (221.67,194.13) -- cycle ; 
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ] (141.76,43.47) -- (266.62,144.19) -- (221.67,194.13) -- cycle ; 
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (181.71,118.8) -- (106.54,118.3) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ]   (204.19,93.83) -- (181.71,118.8) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (201.47,156.4) -- (89.54,155.63) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (235.8,119.4) -- (201.47,156.4) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (162.47,83.07) -- (123.88,82.63) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (174.47,70.07) -- (162.47,83.07) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (211.47,175.73) -- (80.21,174.63) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (211.47,175.73) -- (251.47,132.07) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (191.8,137.07) -- (98.21,136.63) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (220.13,106.4) -- (191.8,137.07) ;
            	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ]   (171.47,99.07) -- (115.21,99.97) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ]   (188.13,81.07) -- (171.47,99.07) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (153.13,65.4) -- (131.54,65.97) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (159.8,58.07) -- (153.13,65.4) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (192.13,138.07) -- (98.21,137.3) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (202.47,157.07) -- (88.88,156.3) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (211.47,176.73) -- (80.21,175.63) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.75 ]   (181.71,118.8) -- (106.54,118.3) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.83 ]   (171.47,99.07) -- (115.21,99.97) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (220.47,107.4) -- (192.13,138.07) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (236.8,120.07) -- (202.47,157.07) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (211.47,176.73) -- (251.47,133.07) ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (141.76,43.47) -- (221.67,194.13) -- (105.47,192.73) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (141.76,43.47) -- (266.62,144.19) -- (191.8,137.07) -- cycle ;
            \\end{tikzpicture}}'''
            % (val_AB, val_AD, val_SA)
        )

        # Nội dung lời giải chi tiết
        loigiai = (
            '''%s
    Ta có diện tích hình chữ nhật $ABCD$ là:\\\\
    $S_{ABCD} = AB \\cdot AD = %s \\cdot %s = %s\\text{ m}^2$.\\\\
    Thể tích của toàn bộ khối chóp $S.ABCD$ là:\\\\
    $V_{S.ABCD} = \\frac{1}{3} \\cdot S_{ABCD} \\cdot SA = \\frac{1}{3} \\cdot %s \\cdot %s = %s\\text{ m}^3$.\\\\
    Vì mặt phẳng $(\\alpha)$ chứa $A$, đi qua $M \\in SB$ và song song với $BD$ nên giao tuyến của $(\\alpha)$ với mặt phẳng $(SBD)$ là đường thẳng đi qua $M$ và song song với $BD$.\\\\
    Do đó $MN // BD$, suy ra theo định lý Thalès trong tam giác $SBD$ ta có:\\\\
    $\\frac{SN}{SD} = \\frac{SM}{SB} = \\frac{2}{3}$.\\\\
    Gọi $O = AC \\cap BD$. Trong mặt phẳng $(SBD)$, đoạn thẳng $SO$ cắt $MN$ tại $I$. Do $MN // BD$ nên:\\\\
    $\\frac{SI}{SO} = \\frac{SM}{SB} = \\frac{2}{3}$.\\\\
    Trong mặt phẳng $(SAC)$, đường thẳng $AI$ cắt cạnh $SC$ tại điểm $P$.\\\\
    Xét tam giác $SAC$, vì $O$ là trung điểm của $AC$ nên $SO$ là đường trung tuyến của tam giác $SAC$. Mặt khác, điểm $I \\in SO$ thỏa mãn $\\frac{SI}{SO} = \\frac{2}{3}$, do đó $I$ chính là trọng tâm của tam giác $SAC$.\\\\
    Vì $AI$ đi qua trọng tâm $I$ nên $AI$ là đường trung tuyến ứng với cạnh $SC$, suy ra $P$ là trung điểm của $SC$, hay:\\\\
    $\\frac{SP}{SC} = \\frac{1}{2}$.\\\\
    Chia khối chóp $S.ABCD$ thành hai khối chóp tam giác $S.ABC$ và $S.ADC$ có thể tích bằng nhau:\\\\
    $V_{S.ABC} = V_{S.ADC} = \\frac{1}{2} V_{S.ABCD} = \\frac{1}{2} \\cdot %s = %s\\text{ m}^3$.\\\\
    Áp dụng công thức tỉ số thể tích Simson cho các khối chóp tam giác:\\\\
    $\\frac{V_{S.AMP}}{V_{S.ABC}} = \\frac{SA}{SA} \\cdot \\frac{SM}{SB} \\cdot \\frac{SP}{SC} = 1 \\cdot \\frac{2}{3} \\cdot \\frac{1}{2} = \\frac{1}{3} \\Rightarrow V_{S.AMP} = \\frac{1}{3} V_{S.ABC}$.\\\\
    $\\frac{V_{S.ANP}}{V_{S.ADC}} = \\frac{SA}{SA} \\cdot \\frac{SN}{SD} \\cdot \\frac{SP}{SC} = 1 \\cdot \\frac{2}{3} \\cdot \\frac{1}{2} = \\frac{1}{3} \\Rightarrow V_{S.ANP} = \\frac{1}{3} V_{S.ADC}$.\\\\
    Suy ra thể tích phần khối chóp phía trên mặt phẳng $(\\alpha)$ là:\\\\
    $V_{S.AMNP} = V_{S.AMP} + V_{S.ANP} = \\frac{1}{3} \\left(V_{S.ABC} + V_{S.ADC}\\right) = \\frac{1}{3} V_{S.ABCD} = \\frac{1}{3} \\cdot %s = %s\\text{ m}^3$.\\\\
    Vậy thể tích khối đa diện $ABCDMNP$ cần tìm là:\\\\
    $V = V_{S.ABCD} - V_{S.AMNP} = %s - %s = %s\\text{ m}^3$.'''
            % (
                tikz_code,
                val_AB, val_AD, val_AB * val_AD,
                val_AB * val_AD, val_SA, latex(V_total),
                latex(V_total), latex(Rational(V_total, 2)),
                latex(V_total), latex(V_tren),
                latex(V_total), latex(V_tren), kq_str
            )
        )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' +
        str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


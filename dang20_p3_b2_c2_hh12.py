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


def bt_dang20_p3_b2_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số: m = O'M và k là tỷ lệ O'B'/O'M
                m = random.randint(2, 6)
                k = random.randint(2, 5)
                a = m * k

                # Kết quả bài toán
                ans_correct = 3 * (m - 1)

                # Đoạn code TikZ vẽ hình lập phương và quỹ đạo (Xóa bỏ toàn bộ comment chứa ký tự % để chống lỗi format)
                tikz_img = ('''\\begin{center}
            \\begin{tikzpicture}[x={(-0.6cm, -0.4cm)}, y={(0.8cm, -0.2cm)}, z={(0cm, 1cm)}, scale=0.6, line width=1pt]
            \\coordinate (O) at (0,0,0);
            \\coordinate (D) at (%s,0,0);
            \\coordinate (B) at (0,%s,0);
            \\coordinate (C) at (%s,%s,0);
            \\coordinate (O') at (0,0,%s);
            \\coordinate (D') at (%s,0,%s);
            \\coordinate (B') at (0,%s,%s);
            \\coordinate (C') at (%s,%s,%s);
            \\coordinate (M) at (%s,0,%s);
            \\coordinate (M1) at (%s,0,%s);
            \\coordinate (M2) at (%s,%s,0);
            \\coordinate (M3) at (%s,%s,0);
            \\coordinate (M4) at (0,%s,%s);
            \\coordinate (M5) at (0,%s,%s);
            \\draw[dashed] (O) -- (D);
            \\draw[dashed] (O) -- (B);
            \\draw[dashed] (O) -- (O');
            \\fill[green!20] (M) -- (M1) -- (M2) -- (M3) -- (M4) -- (M5) -- cycle;
            \\draw (D) -- (C) -- (B);
            \\draw (D') -- (C') -- (B') -- (O') -- cycle;
            \\draw (D) -- (D');
            \\draw (C) -- (C');
            \\draw (B) -- (B');
            \\draw[dashed, red, thick] (M) -- (M1);
            \\draw[red, thick] (M1) -- (M2);
            \\draw[dashed, red, thick] (M2) -- (M3);
            \\draw[red, thick] (M3) -- (M4);
            \\draw[dashed, red, thick] (M4) -- (M5);
            \\draw[red, thick] (M5) -- (M);
            \\fill (M) circle (2pt) node[above left, text=red] {$M$};
            \\fill (M1) circle (2pt) node[left, text=red] {$M_1$};
            \\fill (M2) circle (2pt) node[below left, text=red] {$M_2$};
            \\fill (M3) circle (2pt) node[below right, text=red] {$M_3$};
            \\fill (M4) circle (2pt) node[right, text=red] {$M_4$};
            \\fill (M5) circle (2pt) node[above right, text=red] {$M_5$};
            \\node[below] at (D) {$D$};
            \\node[below right] at (C) {$C$};
            \\node[right] at (B) {$B$};
            \\node[left] at (D') {$D'$};
            \\node[right] at (C') {$C'$};
            \\node[above right] at (B') {$B'$};
            \\node[above left] at (O') {$O'$};
            \\node[below right] at (O) {$O$};
            \\end{tikzpicture}
            \\end{center}''' % (6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                               2, 6, 6, 2, 6, 2, 2, 6, 6, 2, 2, 6))

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho hình lập phương $OBCD.O'B'C'D'$ có cạnh bằng $%s$ sao cho điểm $D$ thuộc tia $Ox$, điểm $B$ thuộc tia $Oy$, và điểm $O'$ thuộc tia $Oz$. Điểm $M$ thuộc cạnh $O'B'$ sao cho $O'B' = %s O'M$. Một con kiến bò từ vị trí $M$ qua sáu mặt của hình lập phương đã cho rồi quay lại vị trí điểm $M$ sao cho quãng đường đi được của con kiến là ngắn nhất. Hỏi với cách bò như vậy, con kiến đã bò qua bao nhiêu điểm mà điểm đó có hoành độ, tung độ và cao độ là các số nguyên dương?
            %s''' % (a, k, tikz_img))

                # Đáp án đúng
                da = str(ans_correct)

                # Tập hợp các đáp án nhiễu
                distractors = set()
                distractors.add(3 * m)
                distractors.add(3 * m + 3)
                distractors.add(3 * (m - 2) if m > 2 else 0)
                distractors.add(6 * m)
                distractors.add(ans_correct + random.choice([1, 2, 3]))
                distractors.add(ans_correct - random.choice([1, 2]))
                distractors.discard(ans_correct)
                distractors.discard(0)

                wrong_choices = random.sample(list(distractors), 3)

                # Gắn đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = '$%s$' % wrong_choices[0]
                da_s2 = '$%s$' % wrong_choices[1] 
                da_s3 = '$%s$' % wrong_choices[2] 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw [line width=1]    (58.86,142.24) -- (163.99,142.24) ;
                		\\draw [line width=1]    (58.86,142.24) -- (59.56,226.02) ;
                		\\draw [line width=1]    (59.56,226.02) -- (164.7,226.02) ;
                		\\draw [line width=1]    (163.99,142.24) -- (164.7,226.02) ;
                		\\draw [line width=1]    (105.21,97.65) -- (210.34,97.65) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (105.21,97.65) -- (105.91,181.43) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (105.91,181.43) -- (211.05,181.43) ;
                		\\draw [line width=1]    (210.34,97.65) -- (211.05,181.43) ;
                		\\draw [line width=1]    (58.86,142.24) -- (105.21,97.65) ;
                		\\draw [line width=1]    (163.99,142.24) -- (210.34,97.65) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (59.56,226.02) -- (105.91,181.43) ;
                		\\draw [line width=1]    (164.7,226.02) -- (211.05,181.43) ;
                		\\draw [line width=1]    (105.21,97.65) -- (105.21,52.25) ;
                		\\draw [shift={(105.21,48.25)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                		\\draw [line width=1]    (59.56,226.02) -- (30.76,253.76) ;
                		\\draw [shift={(27.88,256.53)}, rotate = 316.08] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                		\\draw [line width=1]    (211.05,181.43) -- (253.87,181.97) ;
                		\\draw [shift={(257.87,182.02)}, rotate = 180.72] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                		\\draw  [line width=1]  (319.2,43.31) -- (392.2,43.31) -- (392.2,116.31) -- (319.2,116.31) -- cycle ;
                		\\draw  [line width=1]  (392.2,43.31) -- (465.2,43.31) -- (465.2,116.31) -- (392.2,116.31) -- cycle ;
                		\\draw  [line width=1]  (392.2,116.31) -- (465.2,116.31) -- (465.2,189.31) -- (392.2,189.31) -- cycle ;
                		\\draw  [line width=1]  (465.2,116.31) -- (538.2,116.31) -- (538.2,189.31) -- (465.2,189.31) -- cycle ;
                		\\draw  [line width=1]  (465.2,189.31) -- (538.2,189.31) -- (538.2,262.31) -- (465.2,262.31) -- cycle ;
                		\\draw  [line width=1]  (538.2,189.31) -- (611.2,189.31) -- (611.2,262.31) -- (538.2,262.31) -- cycle ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (349.71,42.87) -- (570.17,261.87) ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (131.33,96.93) .. controls (131.33,95.24) and (132.71,93.87) .. (134.4,93.87) .. controls (136.09,93.87) and (137.47,95.24) .. (137.47,96.93) .. controls (137.47,98.63) and (136.09,100) .. (134.4,100) .. controls (132.71,100) and (131.33,98.63) .. (131.33,96.93) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (346.65,42.87) .. controls (346.65,41.18) and (348.02,39.81) .. (349.71,39.81) .. controls (351.41,39.81) and (352.78,41.18) .. (352.78,42.87) .. controls (352.78,44.57) and (351.41,45.94) .. (349.71,45.94) .. controls (348.02,45.94) and (346.65,44.57) .. (346.65,42.87) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (388.65,85.21) .. controls (388.65,83.51) and (390.02,82.14) .. (391.71,82.14) .. controls (393.41,82.14) and (394.78,83.51) .. (394.78,85.21) .. controls (394.78,86.9) and (393.41,88.27) .. (391.71,88.27) .. controls (390.02,88.27) and (388.65,86.9) .. (388.65,85.21) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (419.65,115.21) .. controls (419.65,113.51) and (421.02,112.14) .. (422.71,112.14) .. controls (424.41,112.14) and (425.78,113.51) .. (425.78,115.21) .. controls (425.78,116.9) and (424.41,118.27) .. (422.71,118.27) .. controls (421.02,118.27) and (419.65,116.9) .. (419.65,115.21) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (461.65,157.21) .. controls (461.65,155.51) and (463.02,154.14) .. (464.71,154.14) .. controls (466.41,154.14) and (467.78,155.51) .. (467.78,157.21) .. controls (467.78,158.9) and (466.41,160.27) .. (464.71,160.27) .. controls (463.02,160.27) and (461.65,158.9) .. (461.65,157.21) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (493.65,189.21) .. controls (493.65,187.51) and (495.02,186.14) .. (496.71,186.14) .. controls (498.41,186.14) and (499.78,187.51) .. (499.78,189.21) .. controls (499.78,190.9) and (498.41,192.27) .. (496.71,192.27) .. controls (495.02,192.27) and (493.65,190.9) .. (493.65,189.21) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (534.65,229.21) .. controls (534.65,227.51) and (536.02,226.14) .. (537.71,226.14) .. controls (539.41,226.14) and (540.78,227.51) .. (540.78,229.21) .. controls (540.78,230.9) and (539.41,232.27) .. (537.71,232.27) .. controls (536.02,232.27) and (534.65,230.9) .. (534.65,229.21) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (566.65,261.21) .. controls (566.65,259.51) and (568.02,258.14) .. (569.71,258.14) .. controls (571.41,258.14) and (572.78,259.51) .. (572.78,261.21) .. controls (572.78,262.9) and (571.41,264.27) .. (569.71,264.27) .. controls (568.02,264.27) and (566.65,262.9) .. (566.65,261.21) -- cycle ;
                		\\draw (84,167.67) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (213.33,158.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (164.7,226.02) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (39.33,209) node [anchor=north west][inner sep=0.75pt]    {$D$};
                		\\draw (80,77.67) node [anchor=north west][inner sep=0.75pt]    {$O'$};
                		\\draw (210,75.67) node [anchor=north west][inner sep=0.75pt]    {$B'$};
                		\\draw (150,119.67) node [anchor=north west][inner sep=0.75pt]    {$C'$};
                		\\draw (40.67,121) node [anchor=north west][inner sep=0.75pt]    {$D'$};
                		\\draw (124,70.33) node [anchor=north west][inner sep=0.75pt]    {$M$};
                		\\draw (236.67,185) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (38,244.33) node [anchor=north west][inner sep=0.75pt]    {$y$};
                		\\draw (84.67,44.33) node [anchor=north west][inner sep=0.75pt]    {$z$};
                		\\draw (300,113) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (374,189) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (448,260.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (294.67,22.33) node [anchor=north west][inner sep=0.75pt]    {$O'$};
                		\\draw (381.33,19) node [anchor=north west][inner sep=0.75pt]    {$B'$};
                		\\draw (464.67,22.33) node [anchor=north west][inner sep=0.75pt]    {$C'$};
                		\\draw (536,94.33) node [anchor=north west][inner sep=0.75pt]    {$C'$};
                		\\draw (610,169.67) node [anchor=north west][inner sep=0.75pt]    {$C'$};
                		\\draw (466.67,92.33) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (529.33,264.33) node [anchor=north west][inner sep=0.75pt]    {$O'$};
                		\\draw (611.2,262.31) node [anchor=north west][inner sep=0.75pt]    {$B'$};
                		\\draw (394.67,118.67) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (465.2,189.31) node [anchor=north west][inner sep=0.75pt]    {$D$};
                		\\draw (337.33,18.33) node [anchor=north west][inner sep=0.75pt]    {$M$};
                		\\draw (394,67.33) node [anchor=north west][inner sep=0.75pt]    {$M_{1}$};
                		\\draw (418.67,91.33) node [anchor=north west][inner sep=0.75pt]    {$M_{2}$};
                		\\draw (467.33,142) node [anchor=north west][inner sep=0.75pt]    {$M_{3}$};
                		\\draw (497.33,167.33) node [anchor=north west][inner sep=0.75pt]    {$M_{4}$};
                		\\draw (541.33,214) node [anchor=north west][inner sep=0.75pt]    {$M_{5}$};
                		\\draw (566.65,265) node [anchor=north west][inner sep=0.75pt]    {$M$};
                	\\end{tikzpicture}
                \\end{center}
             Từ hình trái, sau khi trải phẳng ta thu được hình phải.\\\\
            Vì mặt phẳng $(Oxy) = (OBCD); (Oxz) = (OBB'O'); (Oyz) = (OO'D'D)$ các điểm trên các mặt phẳng trên không thỏa mãn yêu cầu có hoành độ, tung độ và cao độ là các số nguyên dương.\\\\
            Cho nên ta chỉ đếm các điểm có hoành độ dương trên các đoạn thẳng: $M_1 M_2; M_3 M_4; M_5 M$.\\\\
            Ta có tọa độ các điểm: $M(%s; 0; %s); M_1(%s; 0; %s); M_2(%s; %s; 0); M_3(%s; %s; 0); M_4(0; %s; %s); M_5(0; %s; %s)$.\\\\
            Khi đó phương trình đường thẳng $M_1 M_2$ là: $\\begin{cases} x = %s \\\\ y = t \\\\ z = %s - t \\end{cases}$ vì các điểm nằm trên đoạn $M_1 M_2$ nên $0 < t < %s$. Suy ra có $%s$ giá trị $t$ nguyên.\\\\
            Khi đó phương trình đường thẳng $M_3 M_4$ là: $\\begin{cases} x = %s - t \\\\ y = %s \\\\ z = t \\end{cases}$ vì các điểm nằm trên đoạn $M_3 M_4$ nên $0 < t < %s$. Suy ra có $%s$ giá trị $t$ nguyên.\\\\
            Khi đó phương trình đường thẳng $M_5 M$ là: $\\begin{cases} x = t \\\\ y = %s - t \\\\ z = %s \\end{cases}$ vì các điểm nằm trên đoạn $M_5 M$ nên $0 < t < %s$. Suy ra có $%s$ giá trị $t$ nguyên.\\\\
            Khi đó có $3 \\times %s = %s$ điểm thỏa mãn yêu cầu của đề bài.'''
                % (m, a, a, m, a, m, m, a, a, m, m, a,
                   a, m, m, m-1,
                   m, a, m, m-1,
                   m, a, m, m-1,
                   m-1, ans_correct))
                dapan='\\shortans[0]{$%s$}\n'%(ans_correct)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 


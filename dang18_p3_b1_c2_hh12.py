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


def bt_dang18_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo các thiết lập ban đầu
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # a là khoảng cách OA (trong ảnh là 5m)
                # h là chiều cao cột và khoảng cách đến 2 tường (trong ảnh là 1m)
                a_val = random.randint(4, 7)
                h_val = 1

                # Thiết lập hệ trục tọa độ Oxyz với O(0,0,0)
                # A(a, 0, 0), B(0, b, 0), C(0, 0, c)
                # M(h, h, h) là đỉnh cột

                # Phương trình mặt phẳng (ABC): x/a + y/b + z/c = 1
                # Vì M thuộc (ABC) nên: h/a + h/b + h/c = 1 => 1/b + 1/c = 1/h - 1/a
                # Sử dụng Rational để giữ giá trị ở dạng phân số
                k_val = Rational(1, h_val) - Rational(1, a_val)

                # Diện tích S nhỏ nhất khi b = c (do tính đối xứng và BĐT AM-GM)
                # Khi đó: 2/b = k_val => b = 2 / k_val
                b_val = Rational(2, k_val)
                c_val = b_val

                # Tính diện tích nhỏ nhất S_min
                # S = 1/2 * sqrt(a^2*b^2 + b^2*c^2 + c^2*a^2)
                s_exact = (b_val / 2) * sqrt(2 * a_val**2 + b_val**2)

                # Làm tròn đến hàng phần trăm cho đáp án cuối cùng
                kq_float = float(s_exact.evalf())
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                da_dung = str(kq_rounded).replace('.', ',')

                # Bước 4: Tạo các phương án sai
                sai_1 = Decimal(str(kq_float + random.uniform(1.5, 3.5))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                sai_2 = Decimal(str(kq_float - random.uniform(1.5, 3.5))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                if sai_2 <= 0: sai_2 = Decimal(str(kq_float + 5.21))
                sai_3 = Decimal(str(kq_float + random.uniform(4.0, 6.0))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                da_d = '\\True $' + da_dung + '$'
                da_s1 = '$' + str(sai_1).replace('.', ',') + '$'
                da_s2 = '$' + str(sai_2).replace('.', ',') + '$'
                da_s3 = '$' + str(sai_3).replace('.', ',') + '$'

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Bước 2: Nội dung câu hỏi
                noidungcauhoi = (
                    '\\immini{Ông An đang xây một ngôi nhà, trong quá trình xây phải đổ bê tông cho một mái vát để lợp ngói. '
                    'Ông tính toán việc ghép cốt pha đi qua điểm $B$ trên một chân tường và điểm $C$ trên cột góc nhà, '
                    'đồng thời mặt ghép cốt pha phải đi qua điểm $A$ trên chân tường còn lại cách điểm $O$ ở góc giao hai chân tường một khoảng $%s$ m, '
                    'ông cũng tận dụng một chiếc cột có sẵn để chống mặt ghép. Biết rằng hai bức tường được xây vuông góc với nhau, '
                    'mỗi bức tường đều vuông góc với sàn mái nhà, cột có chiều cao $%s$ m và cách hai bức tường với cùng khoảng cách $%s$ m (đỉnh cột là điểm $M$). '
                    'Diện tích nhỏ nhất của khung ghép cốt pha $ABC$ là bao nhiêu mét vuông (làm tròn kết quả đến hàng phần chục)? }'
                    r'''{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (146.47,44.4) -- (146.47,144.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (306.47,144.4) -- (146.47,144.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (66.47,204.4) -- (146.47,144.4) ;
                	\draw [line width=1]    (66.47,204.4) -- (146.47,44.4) ;
                	\draw [line width=1]    (306.47,144.4) -- (146.47,44.4) ;
                	\draw [line width=1]    (66.47,204.4) -- (306.47,144.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (112.47,170.4) -- (175.47,170.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (206.47,144.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (175.47,110.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,110.4) -- (146.47,84.4) ;
                	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (146.47,144.4) ; 
                	\draw [line width=1]    (175.47,110.4) -- (306.47,144.4) ;
                	\draw (306,131) node [anchor=north west][inner sep=0.75pt]    {$A$};
                	\draw (49,202) node [anchor=north west][inner sep=0.75pt]    {$B$};
                	\draw (139,18) node [anchor=north west][inner sep=0.75pt]    {$C$};
                	\draw (125,128) node [anchor=north west][inner sep=0.75pt]    {$O$};
                	\draw (172,86) node [anchor=north west][inner sep=0.75pt]    {$M$};
                	\draw (135,156) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$1m$};
                	\draw (191,152) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$1m$};
                	\draw (157.48,137.48) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize,rotate=-270.13]  {$1m$};
                	\draw (193.27,130.92) node [anchor=north west][inner sep=0.75pt]  [font=\tiny,rotate=-2.4] [align=left] {Chân tường 1};
                	\draw (79.64,179.56) node [anchor=north west][inner sep=0.75pt]  [font=\tiny,rotate=-321.44] [align=left] {Chân tường 2};
                	\draw (133.04,122.01) node [anchor=north west][inner sep=0.75pt]  [font=\tiny,rotate=-269.89] [align=left] {Cột góc nhà};
                \end{tikzpicture} }'''
                    % (latex(a_val), latex(h_val), latex(h_val))
                )

                # Lời giải chi tiết với b, c ở dạng phân số
                loigiai = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (146.47,44.4) -- (146.47,144.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (306.47,144.4) -- (146.47,144.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (66.47,204.4) -- (146.47,144.4) ;
            		\draw [line width=1]    (66.47,204.4) -- (146.47,44.4) ;
            		\draw [line width=1]    (306.47,144.4) -- (146.47,44.4) ;
            		\draw [line width=1]    (66.47,204.4) -- (306.47,144.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (112.47,170.4) -- (175.47,170.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (206.47,144.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (175.47,110.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,110.4) -- (146.47,84.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (175.47,170.4) -- (146.47,144.4) ;
            		\draw [line width=1]    (175.47,110.4) -- (306.47,144.4) ;
            		\draw [line width=1]    (306.47,144.4) -- (329.47,144.4) ;
            		\draw [shift={(332.47,144.4)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (14.21,-4.28) .. controls (9.04,-1.82) and (4.3,-0.39) .. (0,0) .. controls (4.3,0.39) and (9.04,1.82) .. (14.21,4.28)   ;
            		\draw [line width=1]    (66.47,204.4) -- (45.88,219.62) ;
            		\draw [shift={(43.47,221.4)}, rotate = 323.53] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (14.21,-4.28) .. controls (9.04,-1.82) and (4.3,-0.39) .. (0,0) .. controls (4.3,0.39) and (9.04,1.82) .. (14.21,4.28)   ;
            		\draw [line width=1]    (146.47,44.4) -- (146.47,14.4) ;
            		\draw [shift={(146.47,11.4)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (14.21,-4.28) .. controls (9.04,-1.82) and (4.3,-0.39) .. (0,0) .. controls (4.3,0.39) and (9.04,1.82) .. (14.21,4.28)   ;
            		\draw (300,117) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (52,179) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (126,28) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (125,128) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (172,86) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\draw (99,157) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$1$};
            		\draw (205,124) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$1$};
            		\draw (133,76) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$1$};
            		\draw (324,118) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (54.97,212.9) node [anchor=north west][inner sep=0.75pt]    {$y$};
            		\draw (152,8) node [anchor=north west][inner sep=0.75pt]    {$z$};
            	\end{tikzpicture} \end{center}'''
                    'Chọn hệ trục tọa độ $Oxyz$ sao cho $O$ trùng với góc giao giữa hai bức tường, '
                    'các trục $Ox, Oy$ lần lượt nằm trên giao tuyến của hai bức tường với sàn mái nhà, '
                    'trục $Oz$ nằm trên cột góc nhà. \\\\ '
                    'Khi đó, tọa độ các điểm là: $A\\left(%s; 0; 0\\right)$, $B\\left(0; b; 0\\right)$, $C\\left(0; 0; c\\right)$ với $b, c > 0$. \\\\ '
                    'Phương trình mặt phẳng cốt pha $\\left(ABC\\right)$ có dạng: $\\frac{x}{%s} + \\frac{y}{b} + \\frac{z}{c} = 1$. \\\\ '
                    'Đỉnh cột $M$ có tọa độ là $\\left(%s; %s; %s\\right)$. Vì $M$ thuộc mặt phẳng $\\left(ABC\\right)$ nên ta có: \\\\ '
                    '$\\frac{%s}{%s} + \\frac{%s}{b} + \\frac{%s}{c} = 1 \\Leftrightarrow \\frac{1}{b} + \\frac{1}{c} = 1 - \\frac{1}{%s} = \\frac{%s}{%s}$. \\\\ '
                    'Diện tích tam giác $ABC$ với $A(a;0;0), B(0;b;0), C(0;0;c)$ được tính bởi công thức:\\\\ $S = \\frac{1}{2} \\left| \\left[\\vec{AB}, \\vec{AC} \\right] \\right|=\\frac{1}{2}\\sqrt{a^2b^2 + b^2c^2 + c^2a^2} = \\frac{1}{2}\\sqrt{%sb^2 + b^2c^2 + %sc^2}$. \\\\ '
                    'Áp dụng bất đẳng thức AM-GM: $\\frac{%s}{%s} = \\frac{1}{b} + \\frac{1}{c} \\ge 2\\sqrt{\\frac{1}{bc}} \\Rightarrow bc \\ge \\left(\\frac{2 \\cdot %s}{%s}\\right)^2$. \\\\ '
                    'Dấu bằng xảy ra (diện tích nhỏ nhất) khi $b = c$. \\\\ '
                    'Thay $b = c$ vào biểu thức $\\frac{1}{b} + \\frac{1}{c} = \\frac{%s}{%s}$, ta được $\\frac{2}{b} = \\frac{%s}{%s} \\Rightarrow b = c = %s$. \\\\ '
                    'Khi đó diện tích nhỏ nhất là: $S = \\frac{1}{2}\\sqrt{%s \\cdot \\left(%s\\right)^2 + \\left(%s\\right)^2 \\cdot \\left(%s\\right)^2 + %s \\cdot \\left(%s\\right)^2} \\approx %s$ m$^2$.'
                    % (latex(a_val), latex(a_val), latex(h_val), latex(h_val), latex(h_val),
                       latex(h_val), latex(a_val), latex(h_val), latex(h_val), latex(a_val), latex(a_val-h_val), latex(a_val),
                       latex(a_val**2), latex(a_val**2), 
                       latex(a_val-h_val), latex(a_val), latex(a_val), latex(a_val-h_val),
                       latex(a_val-h_val), latex(a_val), latex(a_val-h_val), latex(a_val), latex(b_val),
                       latex(a_val**2), latex(b_val), latex(b_val), latex(c_val), latex(a_val**2), latex(c_val),
                       da_dung)
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(da_dung)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


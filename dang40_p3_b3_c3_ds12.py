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


def bt_dang40_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Cạnh tam giác ABC (chọn số chẵn để diện tích nguyên)
            edge_abc = random.randrange(14, 22, 2)

            # Cạnh tam giác ANP (an_len). Chọn số chẵn để tính toán đẹp.
            # Nếu an_len = 4 thì AM = sqrt(3) giống hệt đề mẫu của bạn.
            an_len = random.choice([4, 6]) 

            # --- BƯỚC 2: TÍNH TOÁN CÁC HỆ SỐ (Tất cả tính theo hệ số của sqrt(3)) ---
            # 1. Chiều cao OA của tam giác đều ANP cạnh an_len: OA = (an_len * sqrt(3))/2
            y_a = Rational(an_len, 2) 

            # 2. Để tiếp xúc tại N, P thì M phải là trung điểm OA => OM = AM = OA/2
            y_m = Rational(an_len, 4) 
            am_val_coeff = Rational(an_len, 4) # Đây là hệ số của sqrt(3) cho AM

            # 3. Tọa độ P(x_p, 0)
            x_p = Rational(an_len, 2)

            # 4. Diện tích ABC: S_abc = (edge^2 * sqrt(3))/4
            s_abc_val = Rational(edge_abc**2, 4)

            # 5. Phương trình Parabol y = ax^2 + y_m*sqrt(3)
            # Đi qua P(x_p, 0) => a = -y_m*sqrt(3) / x_p^2
            a_par_coeff = Rational(-y_m, x_p**2) 

            # 6. Tính diện tích S1 (phần cắt đi ở 1 góc)
            # S1 = tích phân từ 0 đến x_p của |(Đường thẳng AP) - (Parabol)|
            # Đường thẳng AP: y = -sqrt(3)x + y_a*sqrt(3)
            x_sym = symbols('x')
            line_eq = -x_sym + y_a # Đã rút sqrt(3)
            par_eq = a_par_coeff * x_sym**2 + y_m # Đã rút sqrt(3)

            integrand = line_eq - par_eq
            s1_integral = integrate(integrand, (x_sym, 0, x_p))

            # 7. Diện tích mặt bàn S = S_abc - 6*S1
            total_s_coeff = s_abc_val - 6 * s1_integral

            # --- BƯỚC 3: KẾT QUẢ ---
            final_a = int(total_s_coeff)
            final_b = 3
            final_sum = final_a + final_b

            # Định dạng AM để đưa vào đề bài (ví dụ: \sqrt{3} hoặc 3\sqrt{3}/2)
            am_display = latex(am_val_coeff * sqrt(3))

            # --- BƯỚC 4: TIKZ GRAPH ---
            tikz_code = (r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1.5]  (134.53,23.36) -- (231.47,190.24) -- (37.6,190.24) -- cycle ;
            	\draw [line width=1.5]    (37.87,189.44) -- (231.47,190.24) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (165.87,76.99) .. controls (145.4,41.83) and (124.61,41.63) .. (103.47,76.38) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (175.57,190.36) .. controls (212.91,185.12) and (220.79,167.05) .. (199.22,136.12) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (68.75,136.39) .. controls (48.46,169.17) and (57.52,187.14) .. (95.94,190.3) ;
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (106.74,74.7) -- (152.77,148.2) -- (64.24,148.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (161.98,74.87) -- (204.9,148.83) -- (115.57,148.83) -- cycle ;
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (138.06,114.03) -- (180.21,188.08) -- (92.47,188.08) -- cycle ;
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (132.73,123.58) -- (107.74,74.7) -- (161.26,75.49) -- cycle ; 
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (94.72,185.99) -- (69.83,139.81) -- (123.06,140.6) -- cycle ;
            	\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1.5]  (180.21,186.59) -- (153.55,142.32) -- (201.4,143.03) -- cycle ; 
            	\draw [line width=1.5]    (134.53,23.36) -- (134.67,189.84) ;
            	\draw (126,4) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$A$};
            	\draw (21,190) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$B$};
            	\draw (231.47,190.24) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$C$};
            	\draw (125,191) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$H$};
            	\draw (115.92,55) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$M$};
            	\draw (88,58) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$N$};
            	\draw (163,58) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$P$};
            \end{tikzpicture}''')

            # --- BƯỚC 5: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'\immini{Một mặt bàn bằng kính có hình dạng như hình vẽ. Để tạo ra mặt bàn đó người ta dùng một tấm kính hình tam giác đều $ABC$ có cạnh bằng $%s$ dm '
                r'và tại mỗi góc trong tam giác cắt tấm kính theo các đường parabol như nhau. Xét tại đỉnh $A$, parabol có đỉnh $M$ thuộc đường trung tuyến $AH$, '
                r'tiếp xúc với hai cạnh $AB$, $AC$ lần lượt tại $N$, $P$ sao cho $AM = %s$ dm, $AN = AP = %s$ dm. '
                r'Diện tích mặt bàn thu được là một số có dạng $a\sqrt{b}$ (với $a, b \in \mathbb{N}$ và $b$ không có ước chính phương khác $1$). Tổng $a + b$ bằng bao nhiêu?}'
                r'{%s}' % (latex(edge_abc), am_display, latex(an_len), tikz_code))

            # --- BƯỚC 6: LỜI GIẢI CHI TIẾT ---
            loigiai = (r'''Chọn hệ trục $Oxy$ sao cho $A$ nằm trên trục tung, $NP$ nằm trên trục hoành, $O$ là trung điểm $NP$. \\
            Do tam giác $ABC$ đều và $AN = AP = %s$ dm nên tam giác $ANP$ đều. \\
            Suy ra $NP = %s$ dm, chiều cao $OA = %s \cdot \frac{\sqrt{3}}{2} = %s\sqrt{3}$ dm. \\
            Tọa độ các điểm: $A\left(0; %s\sqrt{3}\right)$, $M\left(0; %s\sqrt{3}\right)$ (vì $OM = OA - AM$), $P\left(%s; 0\right)$. \\
            Diện tích tam giác $ABC$ là $S_{ABC} = \frac{%s^2 \sqrt{3}}{4} = %s\sqrt{3}$ (dm$^2$). \\
            Phương trình đường thẳng $AP$: $y = -\sqrt{3}x + %s\sqrt{3}$. \\
            Giả sử parabol đỉnh $M$ có dạng $y = ax^2 + %s\sqrt{3}$. Vì qua $P(%s; 0)$ nên $a = %s\sqrt{3}$. \\
            Diện tích $S_1$ giới hạn bởi $AP$, parabol và trục tung: \\
            $S_1 = \int_{0}^{%s} \left| (-\sqrt{3}x + %s\sqrt{3}) - (%s\sqrt{3}x^2 + %s\sqrt{3}) \right| dx = %s\sqrt{3}$. \\
            Diện tích mặt bàn: $S = S_{ABC} - 6S_1 = %s\sqrt{3} - 6 \cdot %s\sqrt{3} = %s\sqrt{3}$. \\
            Vậy $a = %s, b = %s \Rightarrow a + b = %s$.'''
            % (latex(an_len), latex(an_len), latex(an_len), latex(y_a),
               latex(y_a), latex(y_m), latex(x_p),
               latex(edge_abc), latex(s_abc_val),
               latex(y_a), latex(y_m), latex(x_p), latex(a_par_coeff),
               latex(x_p), latex(y_a), latex(a_par_coeff), latex(y_m), latex(s1_integral),
               latex(s_abc_val), latex(s1_integral), latex(total_s_coeff),
               latex(final_a), latex(final_b), latex(final_sum)))

            # --- BƯỚC 7: ĐÁP ÁN ---
            s = set()
            while len(s) < 3:
                sai = final_sum + random.choice([-5, -2, 2, 5, 10])
                if sai > 0: s.add('$%s$' % sai)
            list_sai = list(s)
            da_d = '\\True $%s$' % final_sum
            list_all = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_all)

            dapan = '\\shortans[0]{$%s$}\n' % final_sum
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang79_p3_b3_c3_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        # Random số lượng áo và đơn giá in để tạo nhiều biến thể bài toán:
        so_ao = random.choice([500, 1000, 1200, 1500, 2000])
        gia_moi_100cm2 = random.choice([30000, 40000, 50000, 60000])

        # Tính toán chính xác
        # Diện tích logo (cm^2):
        s_p1 = float(Rational(64, 3))
        s_tren = 4.0
        s_tron = float(4 * math.pi)
        s_logo = s_p1 - s_tren - s_tron


        chi_phi_nghin_dong = so_ao * (s_logo / 100.0) * (gia_moi_100cm2 / 1000.0)

        # Làm tròn đến hàng đơn vị theo quy tắc ROUND_HALF_UP
        dec_val = Decimal(str(chi_phi_nghin_dong))
        kq = dec_val.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        # Đồ họa TikZ 100% nét đen 1pt theo ảnh mẫu
        tikz_code = ('''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
        		\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (375.27,203.59) .. controls (284.01,25.37) and (192.65,25.33) .. (101.19,203.45) ;
        		\\draw [line width=1]    (101.19,203.45) -- (375.27,203.59) ;
        		\\draw  [line width=1]  (173.61,102.63) .. controls (217.34,124.73) and (260.89,124.39) .. (304.27,101.6) ;
        		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (101.21,205.23) .. controls (101.2,204.64) and (101.19,204.05) .. (101.19,203.45) .. controls (101.19,165.61) and (131.87,134.93) .. (169.71,134.93) .. controls (207.55,134.93) and (238.23,165.61) .. (238.23,203.45) .. controls (238.23,203.77) and (238.23,204.09) .. (238.22,204.41) -- (169.71,203.45) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (101.21,205.23) .. controls (101.2,204.64) and (101.19,204.05) .. (101.19,203.45) .. controls (101.19,165.61) and (131.87,134.93) .. (169.71,134.93) .. controls (207.55,134.93) and (238.23,165.61) .. (238.23,203.45) .. controls (238.23,203.77) and (238.23,204.09) .. (238.22,204.41) ;  
        		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (238.26,204.42) .. controls (238.24,203.83) and (238.24,203.23) .. (238.24,202.64) .. controls (238.24,164.8) and (268.91,134.12) .. (306.76,134.12) .. controls (344.6,134.12) and (375.28,164.8) .. (375.28,202.64) .. controls (375.28,202.96) and (375.27,203.28) .. (375.27,203.59) -- (306.76,202.64) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (238.26,204.42) .. controls (238.24,203.83) and (238.24,203.23) .. (238.24,202.64) .. controls (238.24,164.8) and (268.91,134.12) .. (306.76,134.12) .. controls (344.6,134.12) and (375.28,164.8) .. (375.28,202.64) .. controls (375.28,202.96) and (375.27,203.28) .. (375.27,203.59) ;  
        		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (173.6,101.6) .. controls (203.29,122.94) and (268.84,126.07) .. (304.27,101.6) .. controls (319.22,114.44) and (322.78,120.27) .. (340.5,142.42) .. controls (295.66,120.83) and (242.51,142.42) .. (238.23,203.52) .. controls (232.54,147.4) and (187.7,121.93) .. (137.32,141.86) .. controls (149.5,125.25) and (159,111.87) .. (173.6,101.6) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ][line width=1]  (173.6,101.6) .. controls (166.2,114.63) and (168.32,115.84) .. (173.86,136.33) .. controls (156.14,133.56) and (151.16,136.33) .. (137.32,141.86) .. controls (149.5,125.25) and (161.22,111.87) .. (173.6,101.6) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ][line width=1]  (173.6,101.6) .. controls (174.5,117.4) and (182.16,120.27) .. (192.68,137.43) .. controls (174.96,134.67) and (151.16,136.33) .. (137.32,141.86) .. controls (149.5,125.25) and (161.22,111.87) .. (173.6,101.6) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ][line width=1]  (304.27,101.6) .. controls (303.13,119.62) and (292.89,127.47) .. (281.26,140.2) .. controls (301.6,132.27) and (325.83,136.88) .. (340.5,142.42) .. controls (327.59,125.81) and (317.39,111.87) .. (304.27,101.6) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ][line width=1]  (298.42,98.02) .. controls (305.79,110.38) and (309.11,116.17) .. (303.6,135.6) .. controls (321.23,132.97) and (326.73,137.17) .. (340.5,142.42) .. controls (328.38,126.66) and (310.75,107.76) .. (298.42,98.02) -- cycle ;
        		\\draw [line width=1]    (68,203.45) -- (420.27,203.45) ;
        		\\draw [shift={(424.27,203.45)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (68,70.58) -- (424.27,70.58) ;
        		\\draw [line width=1]    (410.12,74.89) -- (409.34,200.59) ;
        		\\draw [shift={(409.32,204.59)}, rotate = 270.36] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [shift={(410.15,70.89)}, rotate = 90.36] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (173.6,101.6) -- (172.93,30.27) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (304.27,101.6) -- (304.27,29.6) ;
        		\\draw [line width=1]    (300.27,29.62) -- (176.93,30.25) ;
        		\\draw [shift={(172.93,30.27)}, rotate = 359.71] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [shift={(304.27,29.6)}, rotate = 179.71] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (68.69,118.95) -- (237.07,118.95) ;
        		\\draw [line width=1]    (68.06,74.58) -- (68.63,114.95) ;
        		\\draw [shift={(68.69,118.95)}, rotate = 269.18] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [shift={(68,70.58)}, rotate = 89.18] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (101.19,230.34) -- (101.19,203.45) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (375.27,230.48) -- (375.27,203.59) ;
        		\\draw [line width=1]    (371.27,230.48) -- (105.19,230.34) ;
        		\\draw [shift={(101.19,230.34)}, rotate = 0.03] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw [shift={(375.27,230.48)}, rotate = 180.03] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
        		\\draw (233.33,234.33) node [anchor=north west][inner sep=0.75pt]  [font=\\small]  {$8$ cm};
        		\\draw (414,127.67) node [anchor=north west][inner sep=0.75pt]  [font=\\small]  {$4$ cm};
        		\\draw (230,9) node [anchor=north west][inner sep=0.75pt]  [font=\\small]  {$4$ cm};
        		\\draw (5,84.33) node [anchor=north west][inner sep=0.75pt]  [font=\\small]  {$1,5$ cm};
        	\\end{tikzpicture}
        \\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Người ta muốn in %d logo cánh dơi lên %d chiếc áo để bán hàng trong một hội chợ triển lãm. Biết rằng logo là một phần của parabol có chiều cao bằng $4\\text{ cm}$ và rộng $8\\text{ cm}$. Từ parabol, người ta khoét phía dưới bằng hai nửa đường tròn bằng nhau để tạo hiệu ứng cho cánh dơi. Phần phía trên người ta cắt bỏ một phần bằng một đường parabol sao cho vết cắt rộng $4\\text{ cm}$ và đỉnh parabol sâu $1,5\\text{ cm}$ như hình vẽ. Chi phí in một chiếc logo là %d đồng cho mỗi $100\\text{ cm}^2$. Chi phí in hết số logo này theo đơn vị nghìn đồng bằng bao nhiêu? (kết quả làm tròn đến hàng đơn vị).
    %s''' % (so_ao, so_ao, gia_moi_100cm2, tikz_code))

        # Nội dung lời giải
        loigiai = ('''Chọn hệ trục tọa độ $Oxy$ với gốc $O$ là trung điểm đáy của parabol lớn, trục tung $Oy$ đi qua đỉnh parabol lớn. \\\\
                   Theo bài ra: \\\\
                   - Parabol lớn $(P_1)$ có đỉnh $I(0; 4)$ và đi qua các điểm $(-4; 0)$, $(4; 0)$, có phương trình dạng: \\\\
                   $y = 4 - \\frac{1}{4}x^2$. \\\\
                   Diện tích của hình phẳng giới hạn bởi parabol $(P_1)$ và trục hoành là: \\\\
                   $S_1 = \\int\\limits_{-4}^{4} \\left(4 - \\frac{1}{4}x^2\\right) \\,\\mathrm{d}x = \\frac{64}{3}\\text{ cm}^2$. \\\\
                   - Hai nửa đường tròn phía dưới đều có đường kính bằng $4\\text{ cm}$, bán kính $r = 2\\text{ cm}$. Do đó tổng diện tích của hai phần khoét phía dưới đúng bằng diện tích một hình tròn bán kính $r = 2\\text{ cm}$: \\\\
                   $S_2 = \\pi \\cdot 2^2 = 4\\pi\\text{ cm}^2$. \\\\
                   - Vết cắt phía trên rộng $4\\text{ cm}$ tương ứng với khoảng $x \\in [-2; 2]$. Tại $x = \\pm 2$, ta có $y = 4 - \\frac{1}{4}(2)^2 = 3$. \\\\
                   Vết cắt tạo bởi một parabol $(P_2)$ có đỉnh sâu $1,5\\text{ cm}$ so với đỉnh parabol $(P_1)$, tức là đỉnh của $(P_2)$ có tọa độ $(0; 4 - 1,5) = (0; 2,5)$. \\\\
                   Parabol $(P_2)$ đi qua hai điểm $(-2; 3)$ và $(2; 3)$ có phương trình dạng $y = ax^2 + 2,5$. \\\\
                   Thay $x = 2, y = 3$ vào ta được: $3 = a \\cdot 2^2 + 2,5 \\Rightarrow a = \\frac{1}{8}$, do đó $(P_2): y = \\frac{1}{8}x^2 + 2,5$. \\\\
                   Diện tích phần parabol phía trên bị cắt bỏ là: \\\\
                   $S_3 = \\int\\limits_{-2}^{2} \\left[\\left(4 - \\frac{1}{4}x^2\\right) - \\left(\\frac{1}{8}x^2 + 2,5\\right)\\right] \\,\\mathrm{d}x = \\int\\limits_{-2}^{2} \\left(1,5 - \\frac{3}{8}x^2\\right) \\,\\mathrm{d}x = 4\\text{ cm}^2$. \\\\
                   - Diện tích một chiếc logo cánh dơi là: \\\\
                   $S = S_1 - S_2 - S_3 = \\frac{64}{3} - 4\\pi - 4 = \\frac{52}{3} - 4\\pi \\approx 4,767\\text{ cm}^2$. \\\\
                   - Tổng diện tích logo cần in trên %d chiếc áo là: \\\\
                   $S_{\\text{tổng}} = %d \\cdot S = %d \\cdot \\left(\\frac{52}{3} - 4\\pi\\right)\\text{ cm}^2$. \\\\
                   - Chi phí in hết số logo này tính theo đơn vị nghìn đồng là: \\\\
                   $T = \\frac{S_{\\text{tổng}}}{100} \\cdot \\frac{%d}{1000} \\approx %s\\text{ (nghìn đồng)}$.'''
                   % (so_ao, so_ao, so_ao, gia_moi_100cm2, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content


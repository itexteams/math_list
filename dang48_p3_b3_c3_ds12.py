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


def bt_dang48_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random bán kính R (chọn bội số của 4 để chu kỳ lượng giác triệt tiêu đẹp), chiều cao h
                list_R = [8, 12, 16, 20]
                list_h = [10, 12, 15, 18, 20]
                list_c1 = [100000, 120000, 125000, 150000] # Chi phí sơn phản quang
                list_c2 = [40000, 50000, 60000, 80000]     # Chi phí sơn chống lóa

                R = random.choice(list_R)
                h = random.choice(list_h)
                c1 = random.choice(list_c1)
                c2 = random.choice(list_c2)

                # Tính toán các diện tích (chia cho pi)
                S_xq_pi = 2 * R * h
                S1_pi = 4 * R
                S2_pi = S_xq_pi - S1_pi

                # Tính chi phí
                T_vnd_pi = S1_pi * c1 + S2_pi * c2
                T_vnd = T_vnd_pi * math.pi
                T_mil = T_vnd / 1000000

                # Kết quả làm tròn đến hàng đơn vị
                kq_int = round(T_mil)

                # Định dạng chuỗi hiển thị số tiền có dấu chấm phân cách hàng nghìn
                c1_str = "{:,.0f}".format(c1).replace(',', '.')
                c2_str = "{:,.0f}".format(c2).replace(',', '.')
                T_vnd_pi_str = "{:,.0f}".format(T_vnd_pi).replace(',', '.')

                # Làm tròn số thập phân để hiển thị trong lời giải và thay dấu chấm thành phẩy
                T_mil_dec = Decimal(float(T_mil)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                T_mil_float_str = str(T_mil_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_int)]
                da = du[0]
                s = ['$%s$'%(kq_int + 1),
                     '$%s$'%(kq_int + 2),
                     '$%s$'%(kq_int + 3),
                     '$%s$'%(kq_int - 1),
                     '$%s$'%(kq_int - 2),
                     '$%s$'%(kq_int - 3)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center}
            	\tikzset {_03211xuo1/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_4w1livum4}{150bp}{rgb(0bp)=(0,0.5,0);
            		rgb(37.5bp)=(0,0.5,0);
            		rgb(37.75bp)=(0,0.5,0);
            		rgb(45.60714176722935bp)=(1,1,0);
            		rgb(62.5bp)=(0,0.5,0);
            		rgb(100bp)=(0,0.5,0)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            		\path  [shading=_4w1livum4,_03211xuo1] (588.5,83.67) -- (588.5,190.63) .. controls (588.5,203.48) and (535.65,213.9) .. (470.45,213.9) .. controls (405.25,213.9) and (352.4,203.48) .. (352.4,190.63) -- (352.4,83.67) .. controls (352.4,70.82) and (405.25,60.4) .. (470.45,60.4) .. controls (535.65,60.4) and (588.5,70.82) .. (588.5,83.67) .. controls (588.5,96.53) and (535.65,106.95) .. (470.45,106.95) .. controls (405.25,106.95) and (352.4,96.53) .. (352.4,83.67) ; 	\draw   (588.5,83.67) -- (588.5,190.63) .. controls (588.5,203.48) and (535.65,213.9) .. (470.45,213.9) .. controls (405.25,213.9) and (352.4,203.48) .. (352.4,190.63) -- (352.4,83.67) .. controls (352.4,70.82) and (405.25,60.4) .. (470.45,60.4) .. controls (535.65,60.4) and (588.5,70.82) .. (588.5,83.67) .. controls (588.5,96.53) and (535.65,106.95) .. (470.45,106.95) .. controls (405.25,106.95) and (352.4,96.53) .. (352.4,83.67) ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (352.4,83.67) .. controls (352.4,70.82) and (405.25,60.4) .. (470.45,60.4) .. controls (535.65,60.4) and (588.5,70.82) .. (588.5,83.67) .. controls (588.5,96.53) and (535.65,106.95) .. (470.45,106.95) .. controls (405.25,106.95) and (352.4,96.53) .. (352.4,83.67) -- cycle ;
            		\draw [color={rgb, 255:red, 9; green, 32; blue, 251 }  ,draw opacity=1 ][line width=2.25]    (354,122) .. controls (371.1,139.4) and (389,194.71) .. (428.6,208.9) .. controls (468.2,223.09) and (505.37,155.8) .. (544.1,140.9) .. controls (582.83,126) and (579.89,170.93) .. (588.6,164.4) ;
            		\draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (352.4,190.63) .. controls (352.36,190.39) and (352.34,190.15) .. (352.34,189.91) .. controls (352.34,177.06) and (405.06,166.64) .. (470.09,166.64) .. controls (535.13,166.64) and (587.84,177.06) .. (587.84,189.91) .. controls (587.84,190.16) and (587.83,190.4) .. (587.79,190.65) -- (470.09,189.91) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][dash pattern={on 4.5pt off 4.5pt}] (352.4,190.63) .. controls (352.36,190.39) and (352.34,190.15) .. (352.34,189.91) .. controls (352.34,177.06) and (405.06,166.64) .. (470.09,166.64) .. controls (535.13,166.64) and (587.84,177.06) .. (587.84,189.91) .. controls (587.84,190.16) and (587.83,190.4) .. (587.79,190.65) ;  
            		\draw [color={rgb, 255:red, 249; green, 7; blue, 7 }  ,draw opacity=0.2 ][line width=2.25]  [dash pattern={on 6.75pt off 4.5pt}]  (353,179) .. controls (378.1,151.4) and (384.6,139.4) .. (406.1,138.9) .. controls (427.6,138.4) and (442.06,160.95) .. (463.1,160.4) .. controls (484.14,159.85) and (499.03,126.23) .. (522.6,126.4) .. controls (546.17,126.57) and (537.1,182.9) .. (587.1,145.9) ;
            		\draw [color={rgb, 255:red, 9; green, 32; blue, 251 }  ,draw opacity=0.31 ][line width=2.25]  [dash pattern={on 6.75pt off 4.5pt}]  (353.1,150.4) .. controls (370.2,167.8) and (381.1,169.4) .. (401.1,163.9) .. controls (421.1,158.4) and (468.1,91.4) .. (504.6,94.4) .. controls (541.1,97.4) and (564.1,146.9) .. (586.6,130.4) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.9 ] (353,179) .. controls (376.1,153.4) and (375.1,190.4) .. (401.1,200.9) .. controls (428.55,209.44) and (440.1,188.9) .. (461.1,182.9) .. controls (477.58,182.9) and (511.35,206.36) .. (522.6,204.9) .. controls (549.35,198.36) and (565.1,153.9) .. (588.1,175.9) .. controls (588.6,185.4) and (588.6,186.4) .. (587.1,193.4) .. controls (556.1,222.4) and (388.1,218.9) .. (353.1,194.4) .. controls (354.1,188.9) and (351.1,185.4) .. (353,179) -- cycle ;
            		\draw [color={rgb, 255:red, 249; green, 7; blue, 7 }  ,draw opacity=1 ][line width=2.25]    (353,179) .. controls (378.1,151.4) and (377.1,202.9) .. (409.1,203.4) .. controls (441.1,203.9) and (444.56,183.95) .. (465.6,183.4) .. controls (486.64,182.85) and (499.03,204.73) .. (522.6,204.9) .. controls (546.17,205.07) and (565.1,149.9) .. (588.1,175.9) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.58 ] (354,122) .. controls (362.1,124.4) and (395.81,206.09) .. (434.1,210.4) .. controls (481.1,226.9) and (551.52,76.8) .. (588.32,168.8) .. controls (588.32,181.8) and (589.6,178.9) .. (587.1,193.4) .. controls (562.1,219.4) and (383.6,220.4) .. (353.1,194.4) .. controls (352.6,171.4) and (351.6,162.4) .. (354,122) -- cycle ;
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Một công ty kiến trúc dự định trang trí một cột trụ đá hình trụ tròn xoay có bán kính đáy $R = %s$ cm và chiều cao $h = %s$ cm. Để tạo điểm nhấn, kỹ sư thiết kế hai dải đèn LED quấn quanh thân cột. Trong hệ tọa độ bề mặt (được thiết lập bằng cách chọn một đường sinh làm trục tung $Oy$ và đường tròn đáy làm trục hoành $Ox$), hình dạng của hai dải đèn LED được mô tả bởi đồ thị của hai hàm số $y_1 = 3\cos\left(\frac{x}{4}\right) + 4$ và $y_2 = 2 + \sin\left(\frac{x}{2}\right)$.
            %s Việc trang trí bề mặt xung quanh cột trụ được chia thành hai phần. Phần diện tích nằm giữa hai dải đèn LED, được sơn bằng sơn phản quang với chi phí $%s$ VNĐ/cm$^2$ còn phần diện tích còn lại của mặt xung quanh cột trụ, được sơn bằng sơn chống lóa với chi phí $%s$ VNĐ/cm$^2$. Hãy tính tổng chi phí theo đơn vị triệu đồng mà công ty cần chi trả để hoàn thiện việc sơn cột trụ trên (Kết quả làm tròn đến hàng đơn vị).'''
                                 % (R, h, hinhve, c1_str, c2_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chu vi đường tròn đáy của cột trụ là $C = 2\\pi R = 2\\pi \\cdot %s = %s\\pi$ (cm)). \\\\
            Bề mặt xung quanh của cột trụ khi trải phẳng trên hệ tọa độ $Oxy$ là một hình chữ nhật với chiều dài $L = 2\\pi R = %s\\pi$ và chiều rộng bằng chiều cao $h = %s$. \\\\
            Diện tích xung quanh của cột trụ là $S_{xq} = 2\\pi R h = 2\\pi \\cdot %s \\cdot %s = %s\\pi$ (cm$^2$). \\\\
            Phần diện tích nằm giữa hai dải đèn LED tương ứng với diện tích hình phẳng giới hạn bởi đồ thị hàm số $y_1$, $y_2$ và các đường thẳng $x = 0$, $x = %s\\pi$. \\\\
            Diện tích phần sơn phản quang là: \\\\
            $S_1 = \\int\\limits_{0}^{%s\\pi} \\left( y_1 - y_2 \\right) \\mathrm{d}x = \\int\\limits_{0}^{%s\\pi} \\left[ \\left( 3\\cos\\left(\\frac{x}{4}\\right) + 4 \\right) - \\left( 2 + \\sin\\left(\\frac{x}{2}\\right) \\right) \\right] \\mathrm{d}x$ \\\\
            $S_1 = \\int\\limits_{0}^{%s\\pi} \\left( 3\\cos\\left(\\frac{x}{4}\\right) - \\sin\\left(\\frac{x}{2}\\right) + 2 \\right) \\mathrm{d}x = \\left( 12\\sin\\left(\\frac{x}{4}\\right) + 2\\cos\\left(\\frac{x}{2}\\right) + 2x \\right) \\bigg|_{0}^{%s\\pi} = %s\\pi$ (cm$^2$). \\\\
            Phần diện tích còn lại sơn chống lóa là: \\\\
            $S_2 = S_{xq} - S_1 = %s\\pi - %s\\pi = %s\\pi$ (cm$^2$). \\\\
            Tổng chi phí cần chi trả là: \\\\
            $T = S_1 \\cdot %s + S_2 \\cdot %s = %s\\pi \\cdot %s + %s\\pi \\cdot %s = %s\\pi$ (VNĐ). \\\\
            Đổi ra triệu đồng: $T \\approx %s$ triệu đồng. \\\\
            Làm tròn đến hàng đơn vị, công ty cần chi trả $%s$ triệu đồng.'''
                           % (R, 2*R,
                              2*R, h,
                              R, h, S_xq_pi,
                              2*R,
                              2*R, 2*R,
                              2*R, 2*R, S1_pi,
                              S_xq_pi, S1_pi, S2_pi,
                              c1_str, c2_str, S1_pi, c1_str, S2_pi, c2_str, T_vnd_pi_str,
                              T_mil_float_str,
                              kq_int))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_int)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


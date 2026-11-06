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


def bt_dang1_p2_b3_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA=SB=SC$. Gọi $O$ là hình chiếu vuông góc của $S$ trên mặt phẳng $(ABC)$.'''

                            %(
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $O$ là tâm đường tròn ngoại tiếp tam giác $ABC$'
            nb_da_1_s = '$O$ là trọng tâm tam giác $ABC$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Hình vẽ \\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                        \\clip(-0.4910931353732354,-2.4668235869327) rectangle (5.78419970873609,2.910471644050242);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.);
                        \\draw [line width=1.pt] (5.,0.)-- (1.,-2.);
                        \\draw [line width=1.pt] (1.,-2.)-- (0.,0.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.32049462953435,-0.6280665695786921)-- (2.32049462953435,2.375949255284542);
                        \\draw [line width=1.pt] (2.32049462953435,2.375949255284542)-- (0.,0.);
                        \\draw [line width=1.pt] (2.32049462953435,2.375949255284542)-- (1.,-2.);
                        \\draw [line width=1.pt] (2.32049462953435,2.375949255284542)-- (5.,0.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.32049462953435,-0.6280665695786921)-- (1.,-2.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.32049462953435,-0.6280665695786921)-- (5.,0.);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.32049462953435,-0.6280665695786921)-- (0.,0.);
                        \\draw (2.1,2.9) node[anchor=north west] {$S$};
                        \\draw (-0.5,0.2699310435476838) node[anchor=north west] {$A$};
                        \\draw (0.7,-2) node[anchor=north west] {$B$};
                        \\draw (5,0.20578835689579983) node[anchor=north west] {$C$};
                        \\draw (2.2,-0.5) node[anchor=north west] {$O$};
                \\end{tikzpicture}
            \\end{center}
                            $O$ là hình chiếu vuông góc của $S$ trên mặt phẳng $(ABC)$ nên $SO \\perp (ABC)$. \\\\
                            Xét ba tam giác $SOA, SOB$ và $SOC$ là ba tam giác vuông có chung cạnh $SO$ và $SA=SB=SC$ nên ba tam giác bằng nhau. \\\\
                                Suy ra $OA=OB=OC$ nên $O$ là tâm đường tròn ngoại tiếp tam giác $ABC$.''' 
                            %(
                                ))


            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hình chiếu của $SA$ trên mặt phẳng $(ABC)$ là $OA$'
            th_da_1_s = 'Hình chiếu của $SA$ trên mặt phẳng $(ABC)$ là $OB$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Hình chiếu của $SB$ trên mặt phẳng $(ABC)$ là $OB$'
            th_da_2_s = 'Hình chiếu của $SB$ trên mặt phẳng $(ABC)$ là $OC$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True Hình chiếu của $SC$ trên mặt phẳng $(ABC)$ là $OC$'
            th_da_3_s = 'Hình chiếu của $SC$ trên mặt phẳng $(ABC)$ là $OA$'
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2,th_da_3]

            # Nội dung lời giải
            loigiai_th_1 = ('''Hình chiếu của $SA$ trên mặt phẳng $(ABC)$ là $OA$.''' 
                            %(
                                ))
            loigiai_th_2 = ('''Hình chiếu của $SB$ trên mặt phẳng $(ABC)$ là $OB$.''' 
                            %(
                                ))
            loigiai_th_3 = ('''Hình chiếu của $SC$ trên mặt phẳng $(ABC)$ là $OC$.''' 
                            %(
                                ))
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2,loigiai_th_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $SA \\perp BC$ khi $OA \\perp BC$'
            vd_da_1_s = '$SA \\perp BC$ khi $OB \\perp BC$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $SB \\perp AC$ khi $OB \\perp AC$'
            vd_da_2_s = '$SB \\perp AC$ khi $OC \\perp AC$'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True $SC \\perp AB$ khi $OC \\perp AB$'
            vd_da_3_s = '$SC \\perp AB$ khi $OA \\perp AB$'
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2,vd_da_3]

            # Nội dung lời giải
            loigiai_vd_1 = ('''$OA$ là hình chiếu vuông góc của $SA$ trên mặt phẳng $(ABC)$.
                            Khi đó nếu $OA \\perp BC$ thì theo định lí ba đường vuông góc ta có $SA \\perp BC$.''' 
                            %(
                                ))
            loigiai_vd_2 = ('''$OB$ là hình chiếu vuông góc của $SB$ trên mặt phẳng $(ABC)$.
                            Khi đó nếu $OB \\perp AC$ thì theo định lí ba đường vuông góc ta có $SB \\perp AC$.''' 
                            %(
                                ))
            loigiai_vd_3 = ('''$OC$ là hình chiếu vuông góc của $SC$ trên mặt phẳng $(ABC)$.
                            Khi đó nếu $OC \\perp AB$ thì theo định lí ba đường vuông góc ta có $SC \\perp AB$.''' 
                            %(
                                ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2,loigiai_vd_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Hình chiếu của tam giác $SAB$ trên mặt phẳng $(ABC)$ là $OAB$'
            vdc_da_1_s = 'Hình chiếu của tam giác $SAB$ trên mặt phẳng $(ABC)$ là $OAC$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Hình chiếu của tam giác $SBC$ trên mặt phẳng $(ABC)$ là $OBC$'
            vdc_da_2_s = 'Hình chiếu của tam giác $SBC$ trên mặt phẳng $(ABC)$ là $OAB$'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Hình chiếu của tam giác $SAC$ trên mặt phẳng $(ABC)$ là $OAC$'
            vdc_da_3_s = 'Hình chiếu của tam giác $SAC$ trên mặt phẳng $(ABC)$ là $OBC$'
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Hình chiếu của tam giác $SAB$ trên mặt phẳng $(ABC)$ là $OAB$.''' 
                            %(
                                ))
            loigiai_vdc_2 = ('''Hình chiếu của tam giác $SBC$ trên mặt phẳng $(ABC)$ là $OBC$.''' 
                            %(
                                ))
            loigiai_vdc_3 = ('''Hình chiếu của tam giác $SAC$ trên mặt phẳng $(ABC)$ là $OAC$.''' 
                            %(
                                ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

